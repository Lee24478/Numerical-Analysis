import numpy as np

m,n = 4,6
#A = np.array( [[0,-2,-1,-1],[-3,0,2,4],[0,4,-1,1],[-2,4,2,4],] , dtype = float )
A = np.array( np.random.randint(-9,10,(m,n)) , dtype = float )
oA = A.copy()
r = 0
eps = 1.0e-7
E = list( range(m) )
F = list( range(n) )             #是 "n" 唷

for j in range(m):
    if np.max( abs( A[r:,r:] ) ) < eps : continue
    k = np.argmax( abs( A[r:,r:] ) )
    p = r + k//(n-r)
    q = r + k%(n-r)
    if p > r :
        A[ [r,p],: ] = A[ [p,r],: ]
        E[r] = p
    if q > r :
        A[ :,[r,q] ] = A[ :,[q,r] ]
        F[r] = q
    for i in range(r+1,m):
        temp = A[i,j]/A[r,j]
        A[i,r] = temp
        A[i,j+1:] -= temp*A[r,j+1:]
    r += 1
    #if r >= min(m,n) : break

L = np.identity(m , dtype = float)
P = np.identity(m , dtype = float)
Q = np.identity(n , dtype = float)        #是 "n" 唷
for j in range(m):
    L[j+1:,j] = A[j+1:,j]
    A[j+1:,j] = 0
for i in range(m):
    P[ [i,E[i]],: ] = P[ [E[i],i],: ]          #列對調
for i in range(n):                      #是 "n" 唷
    Q[ :,[i,F[i]] ] = Q[ :,[F[i],i] ]         #行對調
print('P =\n' , P.round(4))
print('--------------------------------------------------------------------------')
print('A =\n' , oA.round(4))
print('--------------------------------------------------------------------------')
print('Q =\n' , Q.round(4))
print('--------------------------------------------------------------------------')
print('L =\n' , L.round(4))
print('--------------------------------------------------------------------------')
print('U =\n' , A.round(4))
print('--------------------------------------------------------------------------')
print('PAQ =\n' , np.dot( np.dot(P,oA) , Q ))
print('--------------------------------------------------------------------------')
print('LU =\n' , np.dot(L,A))
