### Mtheta''+Ktheta =Te^{i\Omegat} ###

import matplotlib.pyplot as plt
import numpy as np
import control

# %% Model settings
N = 5  # number of masses
m = 1  # [kg]
k = 1  # [N/m]
c = 0
BC =  'CLAMPED-FREE'
F = 1

# %% Build system matrix

A = [[0,1],[-k/m,-c/m]]
B = [[0],[1/m]]
C = [[1,0]]


sys = control.StateSpace(A,B,C,0)
print(sys)
G1 = control.ss2tf(A,B,C,0)
print(G1)



w = np.logspace(-1, 1.5, 10000)
mag1,phase1,omega1 = control.bode(G1,w,Hz=True,dB=True,deg=True)



################################

# %% Build system matrix
pairwise = np.zeros([N, N])

for i in range(N-1):
    pair = np.array([[1, -1],
                     [-1, 1]])
    pairwise[i:(i+2), i:(i+2)] += pair
    

if N==1:
    M = m*np.eye(1)
    K = k*np.eye(1)
    C = c*np.eye(1)
    invM = 1/M*np.eye(1) 
else:
    M = m * np.eye(N)
    K = k*pairwise
    C = c*pairwise
    invM = np.linalg.inv(M)



if BC == 'CLAMPED-FREE':
        # delete first row, equivalent to MATLAB's A(1, :) = []
        invM = np.delete(invM, 0, 0)
        K = np.delete(K, 0, 0)
        C = np.delete(C, 0, 0)
        # delete first column, equivalent to MATLAB's A(:, 1) = []
        invM = np.delete(invM, 0, 1)
        K = np.delete(K, 0, 1)
        C = np.delete(C, 0, 1)



A = np.vstack((
    np.hstack((np.zeros((N-1, N-1)), np.eye(N-1) )),
    np.hstack((-invM.dot(K), -invM.dot(C)  ))
))




B = np.zeros((2*(N-1), 1))
B[N-1:,0] = 1/m
# print("B:\n", B)

C = np.zeros((1,2*(N-1)))
C[0,0] = 1
# print("C:\n", C)



sys = control.StateSpace(A,B,C,0)
print(sys)
G = control.ss2tf(A,B,C,0)
print(G(0))
print(G)


w = np.logspace(-1, 1.5, 10000)
mag,phase,omega = control.bode(G,w,Hz=True,dB=True,deg=True)


plt.show()