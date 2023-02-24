import numpy as np
import matplotlib.pyplot as plt

q = 0.5*1.225*60.**2.
S = 15.
e = 0.2
Cl_0 = 0.3
Cl_a = 2*np.pi
c = 0.9
Cmca = -3.
Ka = 100000. #costante elastica torsionale
M0 = q*S*(e*Cl_0+c*Cmca)

### Iterative method ###
theta = [0,M0/Ka]
i = 1
tol = 1e-6
theta2 = [0,M0/Ka]
while (abs(theta[i-1]-theta[i])>tol):
    i += 1
    Mat = q*e*S*Cl_a*theta[i-1]
    M = M0 + Mat
    theta.append(M/Ka)
    
for j in range(1,18):
    theta2.append((M0 + q*e*S*Cl_a*theta[j])/Ka)


### Comparison of aeroelastic and rigid lift ###
N = 100 #number of points 
q_qD = np.linspace(0, 1, N)
y = 1*(1/(1-q_qD))
u_uD = np.linspace(0, 1, N)
y2 = 1*(1/(1-u_uD**2))
M=12
thalph = np.array([0.001,0.002,0.003,0.006,0.01,0.02,0.03,0.06,0.1,0.2,0.3,0.5])

results = thalph[:, np.newaxis] * y



### Plots ###

plt.semilogy(q_qD,y,color="blue",label="f(q/q_D)")
plt.semilogy(u_uD,y2,color="red",label="f(U/U_D)")
plt.grid(True)
plt.legend(loc="upper left")
plt.show()

cmap = plt.get_cmap('jet')
for i in range(M):
    plt.semilogy(q_qD, results[i, :], label=f'a = {thalph[i]:.2f}', color=cmap(i/M))
sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(0,0.5))
sm.set_array([])
plt.colorbar(sm, ticks=np.array([0.001,0.005,0.025,0.1,0.5]), label='a')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f')
plt.show()




print('Dynamic pressure q:  ', q)
qd = Ka/(e*S*Cl_a)
print('Divergence dynp qd:  ',qd)
ti = M0/Ka*(q/qd)**i + (1-(q/qd)**i)*M0/(Ka-q*e*S*Cl_a)
print('Iterative solution theta:  ', theta[-1])
print('Complete solution thetai:  ',ti)
plt.plot(theta,color="blue",label="feedback sol")
#plt.plot(theta2,color="red",label="linear difference")
plt.legend(loc="best")
plt.show()

