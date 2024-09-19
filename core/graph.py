import os
import matplotlib.pyplot as plt
from datetime import datetime

import data.simulations.sim_statistic as stat

def create_stat(save_dir='data/simulations'):
    data = stat.data
    
    # Разделяем данные на отдельные переменные
    health = [item[0] for item in data]
    infected = [item[1] for item in data]
    dead = [item[2] for item in data]
    
    # Индексы
    ticks = range(len(data))
    
    # Создаем график
    plt.figure(figsize=(10, 6))
    
    # Построение линий для каждого параметра
    plt.plot(ticks, health, label='Health', marker='o')
    plt.plot(ticks, infected, label='Infected', marker='o')
    plt.plot(ticks, dead, label='Dead', marker='o')
    
    # Добавляем заголовок и метки осей
    plt.title('Sim Graph')
    plt.xlabel('Ticks')
    plt.ylabel('Count')
    
    # Добавляем легенду
    plt.legend()
    
    # Добавляем сетку для удобства
    plt.grid(True)
    
    # Получаем текущее время и форматируем его для использования в имени файла
    current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f'simulation_{current_time}.png'
    
    # Определяем относительный путь к папке для сохранения
    base_dir = os.path.dirname(__file__) 
    project_dir = os.path.abspath(os.path.join(base_dir, '..'))  # Корневая папка проекта
    save_path = os.path.join(project_dir, save_dir)
    
    # Проверяем, существует ли папка, и создаем её, если нет
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    # Формируем полный путь к файлу
    filepath = os.path.join(save_dir, filename)
    
    # Сохраняем график в файл с временной меткой
    plt.savefig(filepath)
    
    # Отображаем график
    plt.show()
