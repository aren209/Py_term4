import matplotlib.pyplot as plt
import os

with open("2.dat", "r") as file:
     lines = file.readlines()

lines_count = 0
for line in lines:
    lines_count += 1
# print(lines_count)

all_x = []
all_y = []

for i in range(0, lines_count, 2):
    x = list(map(float, lines[i].split()))
    y = list(map(float, lines[i+1].split()))
    all_x.extend(x)
    all_y.extend(y)

x_min = min(all_x)
x_max = max(all_x)
y_min = min(all_y)
y_max = max(all_y)


output_dir = 'frames'
os.makedirs(output_dir, exist_ok=True)

for i in range(0, lines_count, 2):
    x = list(map(float, lines[i].split()))
    y = list(map(float, lines[i+1].split()))
    
    plt.plot(x, y)
    plt.title(f'Кадр {int(i/2)}')
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.grid(True, which="major", linestyle='-', alpha=0.5)
    plt.minorticks_on()
    # plt.show()
    
    filename = os.path.join(output_dir, f'frame_{int(i/2):03d}.png')
    plt.savefig(filename)
    plt.close()