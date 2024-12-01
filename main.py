from production_line import LineProduction

if __name__ == "__main__":
    # Parâmetros de entrada
    buffer_capacity = 10
    num_producers = 2
    num_consumers = 3
    timesteps = 100

    # Inicializa e executa a simulação
    simulation = LineProduction(buffer_capacity, num_producers, num_consumers, timesteps)
    results = simulation.run()

    # Relatório
    print("\n=== Resultados Finais ===")
    print(f"Total Produzido: {results['total_produced']}")
    print(f"Total Consumido: {results['total_consumed']}")
    print(f"Itens Restantes no Buffer: {results['final_buffer']}")
