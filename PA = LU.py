import numpy as np

m,n = 4,4
A = np.array([ [0,-2,-1,-1], [-3,0,2,4], [0,4,-1,1], [-2,4,2,4] ] , dtype = float)
oA = A.copy()
r = 0
eps = 1.0e-7
E = list( range(m) )

for j in range (m):
    if max( abs(A[r:,j]) ) < eps : continue
    p = np.argmax( abs(A[r:,j]) ) + r
    if p > r :
        A[ [r,p],: ] = A[ [p,r],: ]
        E[r] = p
    for i in range (r+1,m):
        temp = A[i,j] / A[r,j]
        A[i,r] = temp
        A[i,j+1:] -= temp*A[r,j+1:]
    r += 1

L = np.identity(m , dtype = float)
for j in range(r):
    L[j+1:,j] = A[j+1:,j]
    A[j+1:,j] = 0
print('L =\n' , L.round(4))
print('----------------------------------------------------------------------')
print('U =\n' , A.round(4))
print('----------------------------------------------------------------------')
print('A =\n' , oA)
for i in range(m):
    oA[ [i,E[i]],: ] = oA[ [E[i],i],: ]
print('----------------------------------------------------------------------')
print('PA =\n' , oA)
print('----------------------------------------------------------------------')
print( 'LU =\n' , np.dot(L,A) )
