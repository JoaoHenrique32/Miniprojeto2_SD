Funcionalidades:
-Produção e consumo de itens por múltiplas threads.
-Controle de acesso ao buffer compartilhado com semáforos e locks.
-Relatório de produção, consumo e estado do buffer ao longo do tempo.
-Gráfico visual mostrando o desempenho da simulação.


Requisitos do Sistema:
Python 3.12.6 ou superior
Bibliotecas necessárias:
matplotlib para gráficos.

# antes de tudo, acessar a VENV do projeto
usando o comando no terminal para baixar a venv:
python -m venv venv

e para se conectar a ela você utiliza o comando:
venv\Scripts\activate no Windows
source venv/bin/activate no Linux ou macOS


Para instalar as dependências:
bash ou terminal
pip install matplotlib


Como Usar
Clone este repositório para a sua máquina local:
bash

git clone 
cd Miniprojeto2_SD

Edite os parâmetros no arquivo principal para ajustar a simulação (opcional):
python

# Parâmetros de configuração
BUFFER_CAPACITY = 10        # Capacidade do buffer
NUM_PRODUCERS = 2           # Número de produtores
NUM_CONSUMERS = 3           # Número de consumidores
NUM_TIMESTEPS = 10          # Número de ciclos (timesteps)


Execute o código:
bash ou terminal
python main.py


# Saída do Programa
Durante a execução, o programa exibe:
Tamanho do buffer em cada timestep.
Número de itens produzidos e consumidos.

Ao final, um relatório consolidado mostra:
Total de itens produzidos e consumidos.
Itens restantes no buffer.
Um gráfico é gerado para visualizar o estado do buffer, produção e consumo ao longo do tempo.

# Exemplo de Uso
Com as configurações padrão(alteradas dentro do proprio codigo):

Capacidade do Buffer: 10
Produtores: 2
Consumidores: 3
Timesteps: 10


Saída Esperada:
Timestep 1/10
Estado do buffer: 2 itens no buffer
Itens Produzidos nesta rodada: 2
Itens Consumidos nesta rodada: 0
...
Relatório Final:
Total Produzido: 20 itens
Total Consumido: 18 itens
Itens Restantes no Buffer: 2 itens


# Gráfico Gerado
O gráfico mostra:

Número de itens no buffer.
Itens produzidos por timestep.
Itens consumidos por timestep.