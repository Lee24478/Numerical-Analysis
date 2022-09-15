import numpy as np

#A = np.array([[3,0,8,7,8,25],[-6,-6,8,10,8,16],[-15,-4,-24,29,24,-1],[-6,-2,-8,12,10,2],[-9,2,-32,28,25,-2],[15,8,8,3,8,37]],dtype = float)
m,n = 6,6
A = np.array(np.random.randint(-9,10,(m,n)) , dtype = float)
print(A)
R = A.copy()
eps = 1.0e-7
v = np.zeros(m)
Q = np.identity(m)
r = 0
V = np.zeros((m,n))
Z = np.zeros((m,n))
z = np.zeros(m)
for i in range(m):               #有幾列做幾次
    v[r:] = R[r:,i]
    v[:r] = 0
    L = np.linalg.norm(v)
    if L < eps :
        print('---------------------------v%s = 0---------------------------' %(i+1))
        continue
    y = np.zeros(m)
    if v[r] < 0 : y[r] = L
    else : y[r] = -L
    v -= y
    v1 = v.reshape(m,1)
    vT = v.reshape(1,m)
    V[:,i] = v
    Z[:,i] = 2/np.dot(vT,v1)*v
    print('第%s次' %(i+1))
    print('原Z =\n' , Z.round(4))
    Z1 = Z.copy()
    z = Z1[:,i]
    for k in range(i):
        Z[:,i] -= np.dot(z,V[:,k])*Z[:,k]
    print('新Z =\n' , Z.round(4))
    print('------------------------------------------------------------------------')
    p1 = np.identity(m) - 2/np.dot(vT,v1)*np.dot(v1,vT)
    R = np.dot(p1,R)
    #print('做第%s次 =\n' %(i+1) , R.round(4))
    Q = np.dot(Q,p1.T)
    r += 1
print('---vT--- =\n' , (V.T).round(4))
print('Z =\n' , Z.round(4))
print( (np.identity(m) - np.dot(Z,V.T)).round(4) == Q.round(4) )
#print('-----------------------------------------------------------------')
#print('R =\n' , R.round(4))
#print('Q =\n' , Q.round(4))
#print(np.dot(Q,R).round(4) == A)
