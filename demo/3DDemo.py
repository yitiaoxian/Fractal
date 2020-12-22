import numpy as np
import matplotlib.pyplot as plt

stike = np.linspace(50, 150, 24)
ttm = np.linspace(0.5, 2.5, 24)
stike, ttm = np.meshgrid(stike, ttm)
print(stike[:2])

iv = (stike - 100) ** 2 / (100 * stike) / ttm
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(9, 6))
ax = fig.gca(projection='3d')
surf = ax.plot_surface(stike, ttm, iv, rstride=2, cstride=2, cmap=plt.cm.coolwarm, linewidth=0.5, antialiased=True)
ax.set_xlabel('strike')
ax.set_ylabel('time-to-maturity')
ax.set_zlabel('implied volatility')

plt.show()