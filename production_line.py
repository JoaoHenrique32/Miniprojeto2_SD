import time

# Classes fictícias para o exemplo (defina essas no código real)
class Buffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

class Producer:
    def __init__(self, buffer, id):
        self.buffer = buffer
        self.id = id

    def produce(self):
        print(f"Produtor {self.id} produziu um item.")

class Consumer:
    def __init__(self, buffer, id):
        self.buffer = buffer
        self.id = id

    def consume(self):
        print(f"Consumidor {self.id} consumiu um item.")

# Função principal de simulação
def simulate_production_line(buffer_capacity, num_producers, num_consumers, num_timesteps):
    buffer = Buffer(buffer_capacity)
    producers = [Producer(buffer, i) for i in range(num_producers)]
    consumers = [Consumer(buffer, i) for i in range(num_consumers)]

    for t in range(num_timesteps):
        print(f"Timestep {t + 1}/{num_timesteps}")
        for producer in producers:
            producer.produce()
        for consumer in consumers:
            consumer.consume()
        time.sleep(0.1)

    print("Simulação concluída!")

    

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
