import numpy as np
'''
SVD
'''
#A = np.random.randint(-9,10,(m,n))
#A = np.array([[1,1,0],[0,1,-1],[1,0,1],[1,1,0]] , dtype = float)
#A = np.array([[2,-1,-1],[-2,2,2],[1,1,1],[-1,-1,-1]] , dtype = float)          #改
A = np.array([ [-43,-156,-3,-12,40],[-8,45,48,-69,-91],[26,5,27,-72,-6],[1,-82,-27,22,78],[-24,-99,-21,26,52] ] , dtype = float)
m,n = 5,5          #改
print('A =\n' , A)
V , e , Ut = np.linalg.svd(A)
print('特徵值 =' , (e**2).round(4))
print('特徵向量U =\n' , (Ut.T).round(4))
print('VT =\n' , (V.T).round(4))
E = np.dot(np.dot(V.T,A),Ut.T).round(4)
print('E =\n' , E.round(4))
'''
LS
'''
r = 0
eps = 1.0e-7
for i in range( len(e) ) :
    if e[i] > eps : r += 1         # rank of A 
#b = np.random.randint(-9,10,(m,1))
#b = np.array([ [1],[1],[1],[1] ] , dtype = float)
#b = np.array([ [4],[3],[2],[1] ] , dtype = float)          #改
b = np.array([ [-6],[-3],[0],[9],[-4] ] , dtype = float) 
c = np.dot(V.T,b)            # m*1矩陣
print('c =\n' , c.round(4))
c1 = c[:r]
c2 = c[r:]
print('min =' , ((np.linalg.norm(c2))**2).round(4))
Z = np.zeros((n,1))           # n*1矩陣
#Z = np.array(np.random.randint(-9,10,(n,1)) , dtype = float)     #隨機生成剩下的Z驗算會一樣，但x的值會變！(min發生在 Z2 = 0 時)
for i in range(r):
    Z[i,0] = c1[i,0]/e[i]
print('Z =\n' , Z.round(4))
x = np.dot(Ut.T,Z)
print('x =\n' , x.round(4))
print('驗算min :' , ((np.linalg.norm(np.dot(A,x)-b))**2).round(4))
print('驗算min :' , ((np.linalg.norm(np.dot(E,Z)-c))**2).round(4))

