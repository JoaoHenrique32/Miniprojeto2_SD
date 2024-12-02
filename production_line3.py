import threading
import time
import random
import matplotlib.pyplot as plt
from threading import Semaphore, Lock

# Definição das classes do sistema

class Buffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []
        self.mutex = Lock()  # Mutex para sincronizar o acesso ao buffer
        self.space_semaphore = Semaphore(capacity)  # Semáforo para espaço disponível no buffer
        self.item_semaphore = Semaphore(0)  # Semáforo para itens disponíveis no buffer
    
    def add_item(self):
        # Aguardar até haver espaço no buffer
        self.space_semaphore.acquire()
        with self.mutex:  # Protege o acesso ao buffer
            self.items.append(1)  # Adiciona um item (simbolizado por '1')
    
    def remove_item(self):
        # Aguardar até haver um item disponível no buffer
        self.item_semaphore.acquire()
        with self.mutex:  # Protege o acesso ao buffer
            self.items.pop()  # Remove um item do buffer
    
    def get_size(self):
        return len(self.items)

class Producer(threading.Thread):
    def __init__(self, buffer, id, stop_event):
        super().__init__()
        self.buffer = buffer
        self.id = id
        self.produced_count = 0  # Contador de itens produzidos
        self.stop_event = stop_event  # Evento para parar a thread
    
    def run(self):
        while not self.stop_event.is_set():  # Verifica se o stop_event foi acionado
            time.sleep(random.uniform(0.1, 0.5))  # Simula o tempo de produção
            self.buffer.add_item()  # Produz um item e adiciona ao buffer
            self.produced_count += 1
            print(f"Produtor {self.id} produziu um item.")
            self.buffer.item_semaphore.release()  # Libera um item para consumo

class Consumer(threading.Thread):
    def __init__(self, buffer, id, stop_event):
        super().__init__()
        self.buffer = buffer
        self.id = id
        self.consumed_count = 0  # Contador de itens consumidos
        self.stop_event = stop_event  # Evento para parar a thread
    
    def run(self):
        while not self.stop_event.is_set():  # Verifica se o stop_event foi acionado
            time.sleep(random.uniform(0.1, 0.5))  # Simula o tempo de consumo
            self.buffer.remove_item()  # Consome um item do buffer
            self.consumed_count += 1
            print(f"Consumidor {self.id} consumiu um item.")
            self.buffer.space_semaphore.release()  # Libera espaço para produção

# Função de simulação com contagem e relatório
def simulate_production_line(buffer_capacity, num_producers, num_consumers, num_timesteps):
    buffer = Buffer(buffer_capacity)
    stop_event = threading.Event()  # Evento para controlar a parada das threads
    producers = [Producer(buffer, i, stop_event) for i in range(num_producers)]
    consumers = [Consumer(buffer, i, stop_event) for i in range(num_consumers)]
    
    # Inicia as threads de produtores e consumidores
    for producer in producers:
        producer.start()
    
    for consumer in consumers:
        consumer.start()

    # Variáveis para total de itens produzidos e consumidos
    total_produced = 0
    total_consumed = 0
    buffer_sizes = []  # Para registrar o estado do buffer a cada timestep
    produced_items = []  # Contador de itens produzidos por timestep
    consumed_items = []  # Contador de itens consumidos por timestep
    
    # A cada timestep, monitorar a produção e consumo
    for t in range(num_timesteps):
        print(f"Timestep {t + 1}/{num_timesteps}")
        
        # Registra o tamanho do buffer
        buffer_sizes.append(buffer.get_size())
        
        # Registra quantos itens foram produzidos e consumidos
        produced_this_timestep = sum([producer.produced_count for producer in producers])
        consumed_this_timestep = sum([consumer.consumed_count for consumer in consumers])

        produced_items.append(produced_this_timestep)
        consumed_items.append(consumed_this_timestep)
        
        # Exibe o estado atual do buffer e a produção/consumo
        print(f"Estado do buffer: {buffer.get_size()} itens no buffer")
        print(f"Itens Produzidos nesta rodada: {produced_this_timestep}")
        print(f"Itens Consumidos nesta rodada: {consumed_this_timestep}")
        
        # Espera um pouco antes de continuar para o próximo timestep
        time.sleep(0.5)
    
    # Parar as threads
    stop_event.set()

    # Aguardar as threads terminarem
    for producer in producers:
        producer.join()
    
    for consumer in consumers:
        consumer.join()
    
    # Relatório final
    print("\nRelatório Final:")
    print(f"Total Produzido: {sum(produced_items)} itens")
    print(f"Total Consumido: {sum(consumed_items)} itens")
    print(f"Itens Restantes no Buffer: {buffer.get_size()} itens")
    
    # Gerar gráfico do estado do buffer ao longo do tempo
    plt.plot(range(num_timesteps), buffer_sizes, label="Itens no Buffer")
    plt.plot(range(num_timesteps), produced_items, label="Itens Produzidos", linestyle='--')
    plt.plot(range(num_timesteps), consumed_items, label="Itens Consumidos", linestyle='-.')
    plt.xlabel("Timestep")
    plt.ylabel("Quantidade de Itens")
    plt.title("Produção e Consumo ao Longo do Tempo")
    plt.legend()
    plt.show()

# Parâmetros de configuração
BUFFER_CAPACITY = int(input("Digite a capacidade do buffer: "))
NUM_PRODUCERS = int(input("Digite o número de produtores: "))
NUM_CONSUMERS = int(input("Digite o número de consumidores: "))
NUM_TIMESTEPS = int(input("Digite o número de timesteps: "))

# Inicialização
if __name__ == "__main__":
    simulate_production_line(
        buffer_capacity=BUFFER_CAPACITY,
        num_producers=NUM_PRODUCERS,
        num_consumers=NUM_CONSUMERS,
        num_timesteps=NUM_TIMESTEPS
    )
