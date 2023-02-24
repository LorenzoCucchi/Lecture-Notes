import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def E(x, l=1.0):
    return 1/l*(1-np.cos(x[0]))+0.5*x[1]**2

x1 = np.linspace(-3.14,3.14,1000)
x2 = np.linspace(-1,1,1000) 
x1_grid, x2_grid = np.meshgrid(x1, x2)

E_grid = E([x1_grid,x2_grid])


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x1_grid, x2_grid, E_grid, cmap='jet')
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_zlabel('$E$')

# Create the contour plot
fig2, ax2 = plt.subplots()
contour = ax2.contourf(x1_grid, x2_grid, E_grid, cmap='jet', levels=20)
ax2.set_xlabel('$x_1$')
ax2.set_ylabel('$x_2$')
cbar = fig2.colorbar(contour)
cbar.ax.set_ylabel('$E$')
plt.show()