import numpy as np

def Rb(f,a,b,n) :
    R = np.zeros((n+1,n+1))
    h = b-a
    R[0,0] = (f(a)+f(b))*h/2
    for i in range(1,n+1):
        N = 0
        for j in range(2**(i-1)) : N += f(a+h/2+j*h)
        h /= 2
        R[i,0] = R[i-1,0]/2 + h*N
    for j in range(1,n+1):
        c = 1/(4**j-1) ; d = c+1
        for i in range(j,n+1):
            R[i,j] = d*R[i,j-1] - c*R[i-1,j-1]
    return R

f = lambda x : ( 2**( (x-5.1)**2 ) ) / ( (x-6.5)**9 )
n = 7
R = Rb(f , 7.6 , 9 , n)

for i in range(n+1):
    print('2**%d =' %i , end = ' ') 
    for j in range(i+1):
        print('%1.10f' %R[i,j] , end = ' ; ')
    print()

#請列出第四列
print('2**3 =' , end = ' ')
for i in range (n+1):
    print('%1.10f' %R[3,i] , end = ' ; ')
