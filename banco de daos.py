class BancoDeDados:
    """Classe que representa o banco de dados de pedidos"""
    
    def __init__(self):
        self.pedidos = {}
        self._inicializar_dados()
    
    def _inicializar_dados(self):
        """Método privado para inicializar dados de exemplo"""
        self.pedidos = {
            1234: {"status": "Em transporte", "produto": "Notebook Gamer", "cliente": "João Silva"},
            5678: {"status": "Processando", "produto": "Smartphone", "cliente": "Maria Santos"},
            9012: {"status": "Entregue", "produto": "Tablet", "cliente": "Pedro Oliveira"}
        }
    
    def buscar_pedido(self, numero_pedido):
        """
        Método para buscar um pedido no banco de dados
        
        Args:
            numero_pedido (int): Número do pedido a ser buscado
            
        Returns:
            dict: Dados do pedido ou None se não encontrado
        """
        return self.pedidos.get(numero_pedido)
    
    def get_status_pedido(self, numero_pedido):
        """
        Método específico para obter apenas o status do pedido
        
        Args:
            numero_pedido (int): Número do pedido
            
        Returns:
            str: Status do pedido ou mensagem de erro
        """
        pedido = self.buscar_pedido(numero_pedido)
        if pedido:
            return pedido["status"]
        return "Pedido não encontrado"


class SistemaDePedidos:
    """Classe que representa o sistema de gerenciamento de pedidos"""
    
    def __init__(self):
        self.banco_dados = BancoDeDados()
        self.historico_consultas = []
        self.sistema_ativo = True
    
    def solicitar_status_pedido(self, numero_pedido):
        """
        Método principal para processar solicitações de status
        
        Args:
            numero_pedido (int): Número do pedido solicitado
            
        Returns:
            str: Status formatado do pedido
        """
        # Registra a consulta no histórico
        self._registrar_consulta(numero_pedido)
        
        # Consulta o banco de dados
        status = self.banco_dados.get_status_pedido(numero_pedido)
        
        # Formata a resposta
        return self._formatar_resposta(numero_pedido, status)
    
    def _registrar_consulta(self, numero_pedido):
        """
        Método privado para registrar consultas no histórico
        
        Args:
            numero_pedido (int): Número do pedido consultado
        """
        from datetime import datetime
        self.historico_consultas.append({
            'pedido': numero_pedido,
            'timestamp': datetime.now(),
            'tipo': 'consulta_status'
        })
    
    def _formatar_resposta(self, numero_pedido, status):
        """
        Método privado para formatar a resposta ao cliente
        
        Args:
            numero_pedido (int): Número do pedido
            status (str): Status do pedido
            
        Returns:
            str: Resposta formatada
        """
        return f"Status do pedido {numero_pedido}: {status}"


class Cliente:
    """Classe que representa o cliente do sistema"""
    
    def __init__(self, nome):
        self.nome = nome
        self.pedidos_consultados = []
        self.sistema_pedidos = SistemaDePedidos()
    
    def abrir_sistema(self):
        """
        Método que simula o cliente abrindo o sistema
        
        Returns:
            str: Mensagem de confirmação
        """
        return f"Sistema aberto para {self.nome}"
    
    def consultar_status_pedido(self, numero_pedido):
        """
        Método principal para consultar status de pedido
        
        Args:
            numero_pedido (int): Número do pedido a consultar
            
        Returns:
            str: Resposta com status do pedido
        """
        # Registra a consulta
        self.pedidos_consultados.append(numero_pedido)
        
        # Solicita status ao sistema
        resposta = self.sistema_pedidos.solicitar_status_pedido(numero_pedido)
        
        # Exibe a informação na tela
        self._exibir_informacao(resposta)
        
        return resposta
    
    def _exibir_informacao(self, informacao):
        """
        Método privado para exibir informações na tela
        
        Args:
            informacao (str): Informação a ser exibida
        """
        print(f"=== TELA DO CLIENTE ===")
        print(informacao)
        print("=======================")


# Exemplo de uso do sistema
def main():
    """Função principal para demonstrar o sistema em ação"""
    
    # Cria um cliente
    cliente = Cliente("João Silva")
    
    # Cliente abre o sistema
    print(cliente.abrir_sistema())
    print()
    
    # Cliente solicita status do pedido 1234
    resposta = cliente.consultar_status_pedido(1234)
    
    print(f"\nResposta final: {resposta}")


if __name__ == "__main__":
    main()
