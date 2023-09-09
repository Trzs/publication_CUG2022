import numpy as np
from matplotlib import pyplot as plt

# Nodes                32     64     128   
crusher  = np.array([211.4, 106.1,  53.8])
kokkos   = np.array([496.9, 266.4, 125.5])
cuda     = np.array([593.9, 301.2, 149.6])


fig = plt.figure(figsize=(6, 4))
best = crusher[0]
plt.plot(best/np.array([1, 2, 4]), 'k--')
plt.plot(cuda, 'o-', label='Perlmutter, CUDA')
plt.plot(kokkos, 'o-', label='Perlmutter, KOKKOS')
plt.plot(crusher, 'o-', label='Crusher, KOKKOS')
plt.yscale('log')
plt.ylim(50, 700)
plt.yticks(ticks=[50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700], labels=['50', '', '', '', '', '100', '200', '300', '400', '500', '600', '700'])
plt.xlim(-0.4, 2.4)
plt.xticks(ticks=[0, 1, 2], labels=['32', '64', '128'])
plt.grid(which='both')
plt.xlabel('Number of nodes')
plt.ylabel('Total wall time [sec]')
plt.legend()
plt.tight_layout()
plt.show()
