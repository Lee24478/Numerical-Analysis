import numpy as np

n = 5      # n*n 矩陣
A = np.array( np.random.randint(-9,10,(n,n)) , dtype = float )
b = np.array( np.random.randint(-9,10,n) , dtype = float )
#A = np.array([[2,-3,-1],[3,2,-5],[2,4,-1]],dtype = float)
#b = np.array([3,-9,-5],dtype = float)
x = np.zeros(n)
eps = 1.0e-7
r = 0
print('正解 =' , np.linalg.solve(A,b).round(4))
print('====================================================')

for j in range (n) :
    if max( abs( A[r:,j] ) ) < eps : continue
    p = r + np.argmax( abs( A[r:,j] ) )      #A[列,行]
    if p > r :
        A[[r,p],j:] = A[[p,r],j:]
        b[r] , b[p] = b[p] , b[r]
    for i in range (r+1,n) :
        temp = A[i,j]/A[r,j]
        A[i,j:] -= temp*A[r,j:]      
        b[i] -= temp*b[r]
    print(A.round(4))
    print('---------------------------------------------------------------------------------')
    print(b.round(4))
    print('====================================================')
    r += 1
if r < n : print('Ax != b')
if r == n :
    for i in range(n-1,-1,-1) :
        x[i] = ( b[i] - np.sum(A[i,i+1:]*x[i+1:]) )/A[i,i]
print(x.round(4))


        
