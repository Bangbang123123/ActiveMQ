from proton.utils import BlockingConnection

def run_consumer():
    # URL de conexão AMQP com o ActiveMQ Artemis
    url = "amqp://admin:admin@localhost:5672"
    
    # Endereço multicast correspondente ao produtor
    address = "multicast://test-message"

    print("Conectando ao ActiveMQ para escutar mensagens...")
    connection = BlockingConnection(url)
    
    # Cria o receiver apontando para o tópico/multicast
    receiver = connection.create_receiver(address)

    print("Aguardando mensagens... (Pressione Ctrl+C para parar)\n")

    try:
        while True:
            # Aguarda e recebe a próxima mensagem do broker
            event = receiver.receive()
            message = event.message
            
            print(f"[<] Mensagem recebida: '{message.body}'")
            print(f"    Assunto (Subject): {message.subject}")
            print("-" * 40)
            
            # Confirma o recebimento da mensagem (Acknowledge)
            event.delivery.settle()
            
    except KeyboardInterrupt:
        print("\nEncerrando o consumidor...")
    finally:
        connection.close()
        print("Conexão fechada.")

if __name__ == "__main__":
    run_consumer()