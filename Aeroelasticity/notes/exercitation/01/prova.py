import numpy as np
import matplotlib.pyplot as plt

# Define the system parameters
M = np.eye(2)  # identity matrix
K = np.array([[1, -1], [-1, 1]])  # stiffness matrix
T0 = 1.0  # amplitude of applied moment
Omega = 2.0 * np.pi  # frequency of applied moment

# Solve the generalized eigenvalue problem to find natural frequencies and mode shapes
evals, evecs = np.linalg.eig(np.linalg.inv(M) @ K)
omegas = np.sqrt(-evals)
modes = evecs.T

# Define the frequency range to calculate the frequency response function
w = np.linspace(0, 10, 1000)

# Calculate the frequency response function for each natural frequency and mode shape
Hw = np.zeros_like(w, dtype=np.complex128)
for i, omega in enumerate(omegas):
    mode = modes[i]
    num = T0 * mode[0] * omega**2
    den = (1j*w)**2 + 2*0.01*omega*1j*w + omega**2
    Hw += num / den

# Plot the magnitude and phase of the frequency response function
fig, ax = plt.subplots(2, 1)
ax[0].plot(w, abs(Hw))
ax[0].set_ylabel('Magnitude')
ax[1].plot(w, np.angle(Hw))
ax[1].set_ylabel('Phase')
ax[1].set_xlabel('Frequency')
plt.show()
