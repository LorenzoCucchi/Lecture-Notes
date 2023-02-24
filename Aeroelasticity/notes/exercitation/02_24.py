import numpy as np 
import matplotlib.pyplot as plt
import scipy.linalg as la

N = 4
m = 1
k = 1
c = 0.3

M = m * np.eye(N)
pairs = np.zeros((N,N))

for i in range(N-1):
    pair = np.matrix([[1.,-1.],[-1., 1.]])
    j = i+2
    pairs[i:j,i:j] = pairs[i:j,i:j]+pair
    

K = k*pairs
print(K)
print(M)
M_inv = np.linalg.inv(M)
eigvec, eigval = la.eig(np.matmul(-M_inv,K))


print(eigvec)

print(pairs)