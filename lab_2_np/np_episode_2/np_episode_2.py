import numpy as np
import matplotlib.pyplot as plt

def filter(data):
    filtered_data = np.zeros_like(data, dtype=float)
    for i in range(len(data)):
        start = max(0, i - 10 + 1)
        filtered_data[i] = np.mean(data[start:i+1]) #среднее арифметическое
    return filtered_data

def plot(filename):
    data = np.loadtxt(filename, dtype=float)
    
    filtered_data = filter(data)
    
    plt.figure(figsize=(10, 5))
    plt.plot(data, label='Исходные данные', alpha=0.5)
    plt.plot(filtered_data, label='Фильтрованные данные', linewidth=2)
    plt.legend()
    plt.show()

for j in range(1, 4):
    plot(f"signals/signal0{j}.dat")
