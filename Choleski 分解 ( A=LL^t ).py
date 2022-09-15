import numpy as np

n = 5
B = np.array( [ [4,2,0,10,-16],[2,17,-24,29,24],[0,-24,40,-32,-50],[10,29,-32,114,29],[-16,24,-50,-15,115] ] , dtype = float )
A = (B+B.T)/2
L = np.zeros((n,n))
eps = 1.0e-7
for j in range(n):
    temp = A[j,j] - np.sum( L[j,:j]**2 )
    if temp < eps :
        print('%s' %j,'TNND')
        continue
    L[j,j] = np.sqrt(temp)
    for i in range(j+1,n):
        L[i,j] = ( A[i,j] - np.sum( L[i,:j]*L[j,:j] ) ) / L[j,j]
print('L =\n' , L.round(4))
print( A == np.dot(L,L.T) )
