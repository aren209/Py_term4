import numpy as np
import matplotlib.pyplot as plt

def create_matrix(N):
    A = np.zeros((N, N))
    np.fill_diagonal(A, 1)
    for i in range(1, N):
        A[i, i-1] = -1
    return A

# N = 100               
# steps = 255           
# dt = 0.5              


u_0 = np.loadtxt('3.dat')
u = np.zeros((256, len(u_0)))
u[0] = u_0

A = create_matrix(len(u_0))

for n in range(255):
    u[n+1] = u[n] - 0.5 * A.dot(u[n])
    


# plt.figure(figsize=(10, 6))
# for n in range(0, 256):
#     plt.plot(u[n], label=f"Шаг {n}")
# plt.xlabel("x")
# plt.ylabel("u(x)")
# plt.title("Эволюция решения")
# plt.grid(True)
# plt.show()

for n in range(255):
    plt.xlim(0, 50)
    plt.ylim(0, 10)
    plt.plot(u[n], label=f"Квант времени {n}")
    plt.xlabel("x")
    plt.ylabel("u(x)")
    plt.title(f"Квант времени {n}")
    plt.grid(True)
    plt.savefig(f'plots/quant_{n}')
    plt.close()