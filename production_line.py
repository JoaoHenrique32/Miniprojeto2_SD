import threading
import queue
import time
import random

class LineProduction:
    def __init__(self, buffer_capacity, num_producers, num_consumers, timesteps):
        self.buffer = queue.Queue(maxsize=buffer_capacity)
        self.buffer_capacity = buffer_capacity
        self.num_producers = num_producers
        self.num_consumers = num_consumers
        self.timesteps = timesteps
        self.total_produced = 0
        self.total_consumed = 0
        self.lock = threading.Lock()
        self.sem_items = threading.Semaphore(0)
        self.sem_space = threading.Semaphore(buffer_capacity)
        self.production_log = []  # Para análise
        self.consumption_log = []  # Para análise

    def producer(self, producer_id):
        for t in range(self.timesteps):
            self.sem_space.acquire()
            time.sleep(random.uniform(0.01, 0.1))  # Simula produção
            with self.lock:
                self.buffer.put(1)
                self.total_produced += 1
                self.production_log.append((t, producer_id, self.buffer.qsize()))
            self.sem_items.release()

    def consumer(self, consumer_id):
        for t in range(self.timesteps):
            self.sem_items.acquire()
            time.sleep(random.uniform(0.01, 0.1))  # Simula consumo
            with self.lock:
                self.buffer.get()
                self.total_consumed += 1
                self.consumption_log.append((t, consumer_id, self.buffer.qsize()))
            self.sem_space.release()

    def run(self):
        threads = []

        for i in range(self.num_producers):
            t = threading.Thread(target=self.producer, args=(i,))
            threads.append(t)
            t.start()

        for i in range(self.num_consumers):
            t = threading.Thread(target=self.consumer, args=(i,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        return {
            "total_produced": self.total_produced,
            "total_consumed": self.total_consumed,
            "final_buffer": self.buffer.qsize(),
            "production_log": self.production_log,
            "consumption_log": self.consumption_log,
        }
