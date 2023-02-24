import numpy as np
import matplotlib.pyplot as plt

N = 1000 #number of points 
q_qD = np.linspace(0, 1, N)
y = 1*(1/(1-q_qD))
u_uD = np.linspace(0, 1, N)
y2 = 1*(1/(1-u_uD**2))


plt.semilogy(q_qD,y,color="blue",label="f(q/q_D)")
plt.semilogy(u_uD,y2,color="red",label="f(U/U_D)")
plt.grid(True)
plt.legend(loc="upper left")
plt.show()
