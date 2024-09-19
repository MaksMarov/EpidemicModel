import os
import matplotlib.pyplot as plt
from datetime import datetime

import core.sim_statistic as stat

def create_stat(save_dir='data/simulations', show_graph = False):
    data = stat.data

    health = [item[0] for item in data]
    infected = [item[1] for item in data]
    dead = [item[2] for item in data]

    ticks = range(len(data))

    plt.figure(figsize=(10, 6))

    plt.plot(ticks, health, label='Health', marker='o')
    plt.plot(ticks, infected, label='Infected', marker='o')
    plt.plot(ticks, dead, label='Dead', marker='o')

    plt.title('Sim Graph')
    plt.xlabel('Ticks')
    plt.ylabel('Count')

    plt.legend()

    plt.grid(True)

    current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f'simulation_{current_time}.png'

    base_dir = os.path.dirname(__file__) 
    project_dir = os.path.abspath(os.path.join(base_dir, '..'))
    save_path = os.path.join(project_dir, save_dir)

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    filepath = os.path.join(save_dir, filename)

    plt.savefig(filepath)

    if show_graph:
        plt.show()
