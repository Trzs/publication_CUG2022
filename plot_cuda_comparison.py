import numpy as np
from matplotlib import pyplot as plt

cmap = plt.get_cmap("tab10")
def dark_cmap(x):
    c = cmap(x)
    fac = 0.7
    return (fac*c[0], fac*c[1], fac*c[2], c[3])

# MPI ranks        1      2      3      4      5      6      7      8
cuda = np.array([490.6, 400.9, 319.9, 314.2, 313.4, 313.8, 310.4, 310.6])
kokkos = np.array([439, 248.1, 280.2, 279.6, 281.4, 282.3, 279.9, 280])

cuda_base = [301.2]
kokkos_base = [266.4]

fig = plt.figure(figsize=(6, 4))
plt.plot(np.arange(1, 9), cuda_base*8, '--', color=dark_cmap(0))
plt.plot(np.arange(1, 9), kokkos_base*8, '--', color=dark_cmap(0.1))
plt.plot(np.arange(1, 9), cuda, 'o-', label='CUDA')
plt.plot(np.arange(1, 9), kokkos, 'o-', label='KOKKOS')
plt.grid(which='both')
plt.xlabel('MPI ranks per GPU')
plt.ylabel('Total wall time [sec]')
plt.legend()
plt.tight_layout()
plt.show()
