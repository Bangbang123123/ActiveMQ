import time
from proton import Message
from proton.utils import BlockingConnection

def run_producer():
    # URL de conexão AMQP com o ActiveMQ Artemis
    url = "amqp://admin:admin@localhost:5672"
    
    # Endereço ajustado para o Artemis reconhecer como multicast (tópico)
    # Ou você pode usar apenas "test-message" se o endereço já estiver criado no broker
    address = "multicast://test-message"

    print("Conectando ao ActiveMQ via AMQP...")
    connection = BlockingConnection(url)
    sender = connection.create_sender(address)

    print("Iniciando o envio de 5 mensagens (1 por minuto)...")

    for i in range(1, 6):
        corpo_msg = f"Mensagem AMQP número {i} enviada em tempo real."
        
        # Criando a mensagem com opção persistente
        message = Message(
            body=corpo_msg,
            durable=True,
            subject="NotificacaoImportante"
        )

        sender.send(message)
        print(f"[>] Enviado e Persistido: '{corpo_msg}'")

        if i < 5:
            print("Aguardando 1 minuto para a próxima mensagem...\n")
            time.sleep(60)

    connection.close()
    print("Todas as 5 mensagens foram enviadas com sucesso!")

if __name__ == "__main__":
    run_producer()