### Mtheta''+Ktheta =Te^{i\Omegat} ###

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import scipy.linalg as la
from scipy import signal

# %% Model settings
N = 2  # number of masses
m = 1  # [kg]
k = 1  # [N/m]
c = 1
# %% Build system matrix
M = m * np.eye(N)
pairwise = np.zeros([N, N])
w = np.linspace(0, 10, 1000)
for i in range(N-1):
    pair = np.array([[1, -1],
                     [-1, 1]])
    pairwise[i:(i+2), i:(i+2)] += pair

K = k*pairwise
C = c*pairwise

A = np.hstack([np.zeros((2, 2)), np.eye(2)])
B = np.vstack([np.zeros((2, 1)), np.array([[1], [0]])])
C = np.hstack([np.array([[1, 0]]), np.zeros((1, 1))])
D = np.zeros((1, 1))

sys = signal.lti(A, B, C, D)
print(sys)
tf = signal.lti(sys)
#sys = signal.lti(-M, np.zeros((N,N)), K, np.array([[1, 0], [0, 0]]))

# Calculate the frequency response function
w, Hw = signal.freqresp(sys)


fig, ax = plt.subplots(2, 1)
ax[0].plot(w, abs(Hw))
ax[0].set_ylabel('Magnitude')
ax[1].plot(w, np.angle(Hw))
ax[1].set_ylabel('Phase')
ax[1].set_xlabel('Frequency')
plt.show()
