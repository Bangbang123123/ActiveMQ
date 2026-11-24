from proton.utils import BlockingConnection

def run_consumer():
    # URL de conexão AMQP com o ActiveMQ Artemis
    url = "amqp://admin:admin@localhost:5672"
    
    # Endereço multicast correspondente ao produtor
    address = "queue://test-message"

    print("Conectando ao ActiveMQ para escutar mensagens...")
    connection = BlockingConnection(url)
    
    # Cria o receiver apontando para o tópico/multicast
    receiver = connection.create_receiver(address)

    print("Aguardando mensagens... (Pressione Ctrl+C para parar)\n")

    try:
        while True:
            message = receiver.receive()
            
            print(f"[<] Mensagem recebida: '{message.body}'")
            print(f"    Assunto: {message.subject}\n")

            receiver.accept()
    except KeyboardInterrupt:
        print("\nEncerrando o consumidor...")
    finally:
        connection.close()
        print("Conexão fechada.")

if __name__ == "__main__":
    run_consumer()