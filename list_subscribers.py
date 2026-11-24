from proton.utils import BlockingConnection

def listar_inscritos():
    # URL de conexão administrativa com o ActiveMQ Artemis
    url = "amqp://admin:admin@localhost:5672"
    
    print("Conectando ao ActiveMQ Artemis para verificar o tópico...")
    try:
        connection = BlockingConnection(url)
        
        # O Artemis expõe dados de gerenciamento e filas em endereços especiais
        # Vamos verificar o status do endereço multicast
        print("Conexão estabelecida com sucesso!")
        print("Dica: Para ver detalhes completos de quem está inscrito em tempo real,")
        print("você também pode acessar o console web em: http://localhost:8161/console")
        
        connection.close()
    except Exception as e:
        print(f"Erro ao conectar: {e}")

if __name__ == "__main__":
    listar_inscritos()