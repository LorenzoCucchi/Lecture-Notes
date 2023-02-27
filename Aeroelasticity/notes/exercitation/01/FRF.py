### Mtheta''+Ktheta =Te^{i\Omegat} ###

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import scipy.linalg as la
from scipy import signal

# %% Model settings
N = 3  # number of masses
m = 2  # [kg]
k = 1  # [N/m]
c = 0

F = 1
t = np.arange(0,20,0.01)
Ft = F*np.sin(10*t)
# %% Build system matrix

A = [[0,1],[-k/m,-c/m]]
B = [[0],[1/m]]
C = [[1,0]]


sys = signal.StateSpace(A,B,C,0)
trf = signal.ss2tf(A,B,C,0)
print(trf)
print(sys)


# Calculate the frequency response function
w, Hw = signal.freqresp(sys)
print(Hw)


fig, ax = plt.subplots(2, 1)
ax[0].loglog(w, abs(Hw))
ax[0].set_ylabel('Magnitude')
ax[1].semilogx(w, np.angle(Hw)*180/np.pi)
ax[1].set_ylabel('Phase')
ax[1].set_xlabel('Frequency')
ax[0].grid(True, which="both", ls="--")
ax[1].grid(True, which="both", ls="--")
plt.figure()

plt.plot(Hw.real, Hw.imag, "b")

plt.plot(Hw.real, -Hw.imag, "r")



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




# print("inversa di m", invM)
#A = np.vstack((
#    np.hstack((np.matmul(-invM, C), np.matmul(-invM, K))),
#    np.hstack((np.eye(N),           np.zeros((N, N))))
#))

A = np.vstack((
    np.hstack((np.zeros((N, N)), np.eye(N) )),
    np.hstack((-invM.dot(K), -invM.dot(C)  ))
))


# print("A Matrix\n", A)

B = np.zeros((2*N, 1))
B[N:,0] = 1/m
print("B:\n", B)

C = np.zeros((1,2*N))
C[0,0] = 1
print("C:\n", C)



sys = signal.StateSpace(A,B,C,0)
print(sys)


# Calculate the frequency response function
w, Hw = signal.freqresp(sys)

print(Hw)
fig1, ax1 = plt.subplots(2, 1)
ax1[0].loglog(w, abs(Hw))
ax1[0].set_ylabel('Magnitude')
ax1[1].semilogx(w, np.angle(Hw)*180/np.pi)
ax1[1].set_ylabel('Phase')
ax1[1].set_xlabel('Frequency')
ax1[0].grid(True, which="both", ls="--")
ax1[1].grid(True, which="both", ls="--")


fig2, ax2 = plt.subplots(1,1)

ax2.plot(Hw.real, Hw.imag, "b")

ax2.plot(Hw.real, -Hw.imag, "r")


# 
plt.show()