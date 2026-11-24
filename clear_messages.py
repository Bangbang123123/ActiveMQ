from proton.utils import BlockingConnection
from proton._exceptions import Timeout

def purge_messages():
    # URL de conexão AMQP com o ActiveMQ Artemis
    url = "amqp://admin:admin@localhost:5672"
    
    # Endereço que você quer limpar (ex: multicast://test-message)
    address = "multicast://test-message"

    print(f"Conectando ao broker para limpar o endereço: {address}...")
    connection = BlockingConnection(url)
    
    # Define um timeout curto para sabermos quando acabaram as mensagens
    connection.timeout = 2.0 

    try:
        receiver = connection.create_receiver(address)
        count = 0
        
        print("Limpando mensagens pendentes...")
        while True:
            try:
                # Tenta receber a mensagem com limite de tempo de 1 segundo
                message = receiver.receive(timeout=1.0)
                count += 1
                print(f"[{count}] Removida mensagem antiga: {message.body}")
            except Timeout:
                # Se der timeout, significa que não há mais mensagens na fila/tópico
                break
                
        print(f"\nLimpeza concluída com sucesso! Total de mensagens removidas: {count}")
        
    except Exception as e:
        print(f"Erro durante a limpeza: {e}")
    finally:
        connection.close()
        print("Conexão fechada.")

if __name__ == "__main__":
    purge_messages()