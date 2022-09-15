import numpy as np

np.random.seed(543)
n = 4
A = np.array( np.random.randint(1,10,(4,4)) , dtype = float )
#A = np.array( [ [1,-1,-2,0],[-1,2,1,-1],[-2,1,9,-3],[0,-1,-3,9] ] , dtype = float )
A = (A+A.T)/2
print(A)
#A[0,0]*(1*x[0]+10/A[0,0]*x[1]+14/A[0,0]*x[2]+14/A[0,0]*x[3])**2
#A[2,2]*(14/A[2,2]*x[0]+8/A[2,2]*x[1]+1*x[2]+3/A[2,2]*x[3])**2
temp0 = A[0,0]
A[0,:] /= temp0
A[:,0] /= temp0
A[0,0] = 1
for i in [1,2,3]:
    for j in [1,2,3]:
        A[i,j] -= temp0*A[0,i]*A[0,j]
print(A.round(4))
temp1 = A[1,1]
A[1,1:] /= temp1
A[1:,1] /= temp1
A[1,1] = 1
for i in [2,3]:
    for j in [2,3]:
        A[i,j] -= temp1*A[1,i]*A[1,j]
print(A.round(4))
temp2 = A[2,2]
A[2,2:] /= temp2
A[2:,2] /= temp2
A[2,2] = 1
for i in [3]:
    for j in [3]:
        A[i,j] -= temp2*A[2,i]*A[2,j]
print(A.round(4))
