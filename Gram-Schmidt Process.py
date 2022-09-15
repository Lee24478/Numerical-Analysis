import numpy as np

m,n = 5,7
A = np.array([ [3,3,6,6,3,8,3],[4,2,6,6,6,6,4],[5,1,6,0,9,0,-1],[-2,2,0,3,-6,6,1],[0,-3,-3,-6,3,-9,-3] ])
Q = np.zeros((m,n))
R = np.zeros((n,n))
r = 0
eps = 1.0e-7

for j in range(n):
    L = np.linalg.norm(A[:,j])
    if L < eps : continue
    Q[:,r] = A[:,j]
    for i in range(r):
        R[i,j] = np.dot(Q[:,i],A[:,j])
        Q[:,r] -= R[i,j] * Q[:,i]
    L = np.linalg.norm(Q[:,r])
    R[r,j] = L
    if L > eps :
        Q[:,r] /= L
        r += 1

for i in range(r):
    for j in range(i):
        print(i,j,np.dot(Q[:,i],Q[:,j]))     #驗行向量內積為0

print(np.linalg.norm(A - np.dot(Q,R)))       #驗A = QR
print('v向量 =\n' , Q.round(4))
print('R =\n' , R.round(4))

B = Q.T
print('Q.T =\n' , B.round(4))
q = 0
for j in range(r):
    if max( abs(B[q:,j]) ) < eps : continue
    p = q + np.argmax( abs(B[q:,j]) )
    if p > q :
        B[ [p,q],: ] = B[ [q,p],: ]
    for i in range(q+1,r):
        temp = B[i,j]/B[q,j]
        B[i,j:] -= temp * B[q,j:]
    q += 1
    B[j,:]/=B[j,j]
print('消去後 =\n' , B.round(4))


