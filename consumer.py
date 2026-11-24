from proton.utils import BlockingConnection

def run_consumer():
    # Endereços de conexão
    url = "amqp://admin:admin@localhost:5672"
    address = "queue://test-message"

    # Criação da conexão
    connection = BlockingConnection(url)
    receiver = connection.create_receiver(address)

    print("Pressione Ctrl+C para parar de receber mensagens\n\n")

    try:
        # Roda o programa até o usuário pausar com ctrl+c
        while True:
            # Recebe a mensagem
            message = receiver.receive()
            
            print(f"[<] Mensagem recebida: '{message.body}'")
            print(f"    Assunto: {message.subject}\n")

            # Tira a mensagem do buffer
            receiver.accept()
    except KeyboardInterrupt:
        print("\nEncerrando o consumidor...")
    finally:
        # Fechamento da conexão
        connection.close()
        print("Conexão fechada.")

if __name__ == "__main__":
    run_consumer()