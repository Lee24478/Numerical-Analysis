import numpy as np
np.random.seed(543)
n = 5
eps = 1.0e-7
lam = 0
r = 10
#S = [0]

A = np.random.randint(-9,10,(n,n))
print(A)
#A = np.array([ [-4,2,3,-6,-12],[2,-18,-1,-8,4],[3,-1,0,-5,-3],[-6,-8,-5,18,0],[-12,4,-3,0,6] ] , dtype = float)
A += A.T
e = np.linalg.eigvals(A)
print('特徵值 =' , e.round(4))
x = np.array([-5,9,5,6,7] , dtype = float)
#N = np.linalg.norm(A,2)
#x = np.random.randn(n)
#x = np.array([-6,-3,7,3,-2] , dtype = float)
#x = np.array([-2,3,3,-5,-6] , dtype = float)
#x = np.array([4,-9,-6,-2,6] , dtype = float)
#x = np.array([2,5,-2,-5,8] , dtype = float)
#x = np.array([-2,9,-2,1,6] , dtype = float)
xlen = np.linalg.norm(x)
x /= xlen
I = [e[0]-min((e[1]-e[0]),1000)/2 , e[0]+min((e[1]-e[0]),1000)/2]
#I = [e[1]-min((e[1]-e[0]),(e[3]-e[1]))/2 , e[1]+min((e[1]-e[0]),(e[3]-e[1]))/2]
#I = [e[3]-min((e[4]-e[3]),(e[3]-e[1]))/2 , e[3]+min((e[4]-e[3]),(e[3]-e[1]))/2]
#I = [e[4]-min((e[4]-e[3]),(e[2]-e[4]))/2 , e[4]+min((e[4]-e[3]),(e[2]-e[4]))/2]
#I = [e[2]-min(1000,(e[2]-e[4]))/2 , e[2]+min(1000,(e[2]-e[4]))/2]

for i in range(1,50):
        x = np.array([-5,9,5,6,7] , dtype = float)
        b = 2*i+1
        a = (I[1]-I[0])/b
        s = I[0]+(i)*a
        As = A - s*np.identity(n)
        for j in range(10):
                ox = x.copy()
                x = np.linalg.solve(As,x)
                xlen = np.linalg.norm(x)
                x /= xlen                                     #特徵向量
                if np.dot(ox,x) < eps :
                    x *= -1
                    xlen *= -1
                #print('特徵向量 =' , x.round(4))
                if np.linalg.norm(ox-x) < eps :
                    lam = 1/xlen + s                        #特徵值
                    #print('特徵值 =' , lam.round(4))
                    r = j
                    break
                    #print(b)
        if r <= 4 :
                print('特徵值 =' , lam.round(4))
                print(b)
                break
        

