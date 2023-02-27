# %% Packages
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import scipy
from math import *
import cmath
sqrtv = np.vectorize(cmath.sqrt)

# %% Build system matrix
#Jp = 5
#GJ = 1e5
#L = 5.5
Jp = 1
GJ = 1
L = 4

BC = 'CLAMPED-FREE'
#BC = 'FREE-FREE'


    
# Number of elements        
N = 4

li = L/N
# %% Build system matrix

M = np.eye(N)*Jp*li
M_inv = np.diag((1/(Jp*li))*np.ones(N))
K = np.diag(np.ones(N)*2) - np.diag(np.ones(N-1), 1) - np.diag(np.ones(N-1), -1) 
K[0,0] = 1;
K[-1,-1] = 1;

K = K*(GJ/li);

if BC == 'CLAMPED-FREE':
    # delete first row, equivalent to MATLAB's A(1, :) = []
    M_inv = np.delete(M_inv, 0, 0)
    K = np.delete(K, 0, 0)
    # delete first column, equivalent to MATLAB's A(:, 1) = []
    M_inv = np.delete(M_inv, 0, 1)
    K = np.delete(K, 0, 1)

l, v = np.linalg.eig(np.matmul(-M_inv, K))

omega = np.imag(sqrtv(l))
idx = omega.argsort()


f = open("Aeroelasticity/notes/exercitation/01/res.txt", "w")
f.write("Now the file has more content!")

f.write("System ---\n\n")
f.write("Matrices:\n")
f.write("M =\n{0}\n\n".format(M))
f.write("K =\n{0}\n\n".format(K))
f.write("---\n\n")
f.write("Eigenanalysis ---\n\n")
f.write("Eigenvalues and natural frequencies:\n")
f.write("omega_i = {0}\n".format(omega[idx]/2/pi))
f.write("Eigenvectors (mode shapes):\n")
f.write("v =\n{0}\n\n".format(v[:, idx]))
f.write("NOTE: unit norm normalization.\n")
f.write("---\n")

f.close()

# %% Analytical

omegan = lambda n: np.sqrt(GJ/Jp/(L**2))*np.pi/2*(1+2*n)/2/pi
nmodes = np.array([0,1,2,3])
wn = omegan(nmodes)


plt.show()