import matplotlib.pyplot as plt

for j in range(4):
    with open(f"dead_moroz/00{j+1}.dat", "r") as file:
        lines = file.readlines()
        
    num = int(lines[0])
    
    xdata = []
    ydata = []
    
    for i in range(num):
        x, y = map(float, lines[i+1].split())
        xdata.append(x)
        ydata.append(y)
    
    appropriate_size = max(8, 100 - num * 5)
    
    plt.title(f"Количество точек: {num}")
    plt.scatter(xdata, ydata, color='green', s = appropriate_size)
    
    plt.show()
