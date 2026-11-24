import time
from proton import Message
from proton.utils import BlockingConnection

def run_producer():
    # Endereços de conexão
    url = "amqp://admin:admin@localhost:5672"
    address = "queue://test-message"

    # Criação da conexão
    connection = BlockingConnection(url)
    sender = connection.create_sender(address)

    print("Iniciando o envio de 5 mensagens (1 por minuto)...")

    # Envio de 5 mensagens a cada 10 segundos
    for i in range(1, 6):
        corpo_msg = f"Mensagem número {i}"
        
        message = Message(
            body=corpo_msg,
            durable=False,
            subject="Notificacao Teste"
        )

        # Envio da mensagem
        sender.send(message)
        print(f"[>] Enviado: '{corpo_msg}'")

        if i < 5:
            print("Aguardando 10 segundos para a próxima mensagem...\n")
            time.sleep(10)

    # Fechamento da conexão
    connection.close()
    print("Todas as 5 mensagens foram enviadas com sucesso!")

if __name__ == "__main__":
    run_producer()