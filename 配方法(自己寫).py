import numpy as np
import fractions as fr
np.set_printoptions(formatter={'all':lambda x: str(fr.Fraction(x).limit_denominator())})

#np.random.seed(543)
#A = np.array( np.random.randint(1,10,(4,4)) , dtype = float )
#A = np.array( [ [3,-5,4,-2,-2],[-5,-5,0,-1,1],[4,0,3,-1,-2],[-2,-1,-1,0,-2],[-2,1,-2,-2,-1] ] , dtype = float )
#A = np.array( [ [-3,1,-3,2,-3],[1,0,-5,0,5],[-3,-5,1,-4,5],[2,0,-4,-1,5],[-3,5,5,5,-2] ] , dtype = float )
A = np.array( [ [6,2,4,6,6],[2,5,2,8,8],[4,2,1,2,7],[6,8,2,1,2],[6,8,7,2,3] ] , dtype = float )
A = (A+A.T)/2
oA = A.copy()
print('原A =\n' , oA)
print('=========================')

q = [0,1,2,3,4]
n = 5
U = np.zeros((n,n))
for k in [4,0,3,1]:         #隨著題目變動
    temp = A[k,k]
    print('係數 =' , fr.Fraction(temp).limit_denominator())
    A[k,:] /= temp
    A[:,k] /= temp
    A[k,k] = 1
    q.remove(k)
    #print(q)
    for i in q:
        for j in q:
            A[i,j] -= temp*A[k,i]*A[k,j]
    #print(A)
    print('(x%s)^2項 =' %(k) , A[k,:])
    U += temp*np.dot(A[k,:].reshape(n,1),A[k,:].reshape(1,n))
    A[k,:] = 0
    A[:,k] = 0
    print('-------------------------------------')
print('最後一項 =' , A[q[0],:])
U[q[0],:] += A[q[0],:]
print('驗證\n' , U)



