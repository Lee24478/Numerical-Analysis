import numpy as np
import sympy as sy

c = sy.IndexedBase('c')
s = sy.IndexedBase('s')
n = 5
P = np.identity(n , dtype = object)
G = np.identity(n , dtype = object)
for i in range(1,n):
    G[0,0] = c[i]
    G[0,i] = -s[i]
    G[i,0] = s[i]
    G[i,i] = c[i]
    P = np.dot(G,P)
    G[0,0],G[0,i],G[i,0],G[i,i] = 1,0,0,1
print(P)
