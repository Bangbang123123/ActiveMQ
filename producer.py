import time
from proton import Message
from proton.utils import BlockingConnection

def run_producer():
    # URL de conexão AMQP com o ActiveMQ Artemis
    url = "amqp://admin:admin@localhost:5672"
    
    # Endereço ajustado para o Artemis reconhecer como multicast (tópico)
    # Ou você pode usar apenas "test-message" se o endereço já estiver criado no broker
    address = "queue://test-message"

    print("Conectando ao ActiveMQ via AMQP...")
    connection = BlockingConnection(url)
    sender = connection.create_sender(address)

    print("Iniciando o envio de 5 mensagens (1 por minuto)...")

    for i in range(1, 6):
        corpo_msg = f"Mensagem número {i}"
        
        # Criando a mensagem com opção persistente
        message = Message(
            body=corpo_msg,
            durable=False,
            subject="NotificacaoTeste"
        )

        sender.send(message)
        print(f"[>] Enviado: '{corpo_msg}'")

        if i < 5:
            print("Aguardando 10 segundos para a próxima mensagem...\n")
            time.sleep(10)

    connection.close()
    print("Todas as 5 mensagens foram enviadas com sucesso!")

if __name__ == "__main__":
    run_producer()