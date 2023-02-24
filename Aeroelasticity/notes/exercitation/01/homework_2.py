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
L = 1

BC = 'CLAMPED-FREE'
#BC = 'FREE-FREE'

n = 200
res = np.zeros((n-1,4))
count = 0
# %% Analysis
for panels in range(2,n+1):
    
    # Number of elements        
    N = panels

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

    if panels < 5:
        res[count,0:panels-1] = omega[idx[0:panels-1]]/2/pi
    else:
        res[count,:] = omega[idx[0:4]]/2/pi
    count += 1
    #f = open("Lecture-Notes\Aeroelasticity\\notes\exercitation\\01\\res.txt", "w")
    #f.write("Now the file has more content!")
#
    #f.write("System ---\n\n")
    #f.write("Matrices:\n")
    #f.write("M =\n{0}\n\n".format(M))
    #f.write("K =\n{0}\n\n".format(K))
    #f.write("---\n\n")
    #f.write("Eigenanalysis ---\n\n")
    #f.write("Eigenvalues and natural frequencies:\n")
    #f.write("omega_i = {0}\n".format(omega[idx]/2/pi))
    #f.write("Eigenvectors (mode shapes):\n")
    #f.write("v =\n{0}\n\n".format(v[:, idx]))
    #f.write("NOTE: unit norm normalization.\n")
    #f.write("---\n")
#
    #f.close()
 
    # %% Analytical

omegan = lambda n: np.sqrt(GJ/Jp/(L**2))*np.pi/2*(1+2*n)
nmodes = np.array([0,1,2,3])
wn = omegan(nmodes)/2/pi
print(res)
err_m1 = (res[:,0]-wn[0])/wn[0]*100
err_m2 = (res[1::,1]-wn[1])/wn[1]*100
err_m3 = (res[2::,2]-wn[2])/wn[2]*100
err_m4 = (res[3::,3]-wn[3])/wn[3]*100


plt.plot(np.arange(2,n+1),err_m1,label="Mode 1")
print(1)
plt.plot(np.arange(3,n+1),err_m2,label="Mode 2")
print(2)
plt.plot(np.arange(4,n+1),err_m3,label="Mode 3")
print(3)
plt.plot(np.arange(5,n+1),err_m4,label="Mode 4")
plt.title("Error between lumped model and analytical")
plt.ylabel("Error [%]")
plt.legend(loc="best")
plt.grid(True)
plt.show()
