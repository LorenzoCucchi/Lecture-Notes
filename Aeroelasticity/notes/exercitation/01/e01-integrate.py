# %% Packages
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import scipy

# %% Model settings
N = 4  # number of masses
m = 1  # [kg]
k = 1  # [N/m]
c = 0.1  # [Ns/m]

# %% Build system matrix
M = m * np.eye(N)
pairwise = np.zeros([N, N])
for i in range(N-1):
    pair = np.array([[1, -1],
                     [-1, 1]])
    pairwise[i:(i+2), i:(i+2)] += pair

K = k*pairwise
C = c*pairwise

invM = np.linalg.inv(M)
A = np.vstack((
    np.hstack((np.matmul(-invM, C), np.matmul(-invM, K))),
    np.hstack((np.eye(N),           np.zeros((N, N))))
))
print(A)

# %% Eigenvalues
eigval, eigvec = scipy.linalg.eig(K, M, right=True)
complval, complvec = scipy.linalg.eig(A, right=True)

# %% Solve
modenum = 1
x0 = np.zeros(2*N)  # x1' x2' x3' x4' x1 x2 x3 x4
x0[0:N] = eigvec[:, modenum]
angular_frequency = np.sqrt(np.real(eigval[modenum]))
period = 2 * np.pi / angular_frequency


def dx(x, _, A):
    return np.matmul(A, x)


t = np.linspace(0.0, 10.0, 100)
sol = scipy.integrate.odeint(dx, x0, t, args=(A,))

# %% Plot results
fig, ax = plt.subplots()
for i in range(N):
    ax.plot(t, sol[:, i], label='x{}'.format(i+1))
ax.set_title('Mode number {}, period {:.3f}'.format(modenum+1, period))
ax.set_xlabel('time [s]')
ax.set_ylabel('mass position [m]')
ax.legend()
plt.show()



N = 4;  # no of degrees of freedom (moving masses)
m = 1;  # mass [kg] OR [kg * m^2] for torsion
k = 1;  # stiffness [N/m] OR [Nm/rad]
c = 0.3;  #s viscous damping [Ns/m] OR [Nms/rad]
# %% Animate mode
fig, ax = plt.subplots()
ln, = ax.plot([], [], 's', markersize=12)
h_spacing = 2.0


def init():
    ax.set_xlim(0, h_spacing * (N+1))
    ax.set_ylim(-1, 1)
    return ln,


def update(frame):
    xdata = (np.arange(N) + 1) * h_spacing
    xdata += sol[frame, :N]
    ydata = np.zeros(N)
    ln.set_data(xdata, ydata)
    return ln,


ani = FuncAnimation(fig, update, frames=np.arange(t.shape[0]),
                    init_func=init, blit=True, interval=100)
plt.show()
