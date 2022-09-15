import numpy as np

def eva(a,x) :
    n = len(a)-1
    p = a[n]
    dp = 0.0+0.0j
    ddp = 0.0+0.0j
    for i in range (1,n+1) :
        ddp = 2.0*dp + x*ddp
        dp = p + x*dp
        p = a[n-i] + x*p
    return p,dp,ddp

def SD(a,b) :
    n = len(a)-1
    for i in range (1,n+1) :
        a[n-i] += a[n-i+1]*b

def LG(a) :
    n = len(a)-1
    eps = 1.0e-7
    x = np.random.uniform(-9.9,9.9)
    for i in range (30) :
        p,dp,ddp = eva(a,x)
        g = dp/p  ;  h = g**2-ddp/p
        q = np.sqrt((n-1)*(n*h-g**2))
        if abs(g+q) > abs(g-q) : dx = n/(g+q)
        else : dx = n/(g-q)
        x -= dx
        print('{:1.6f}'.format(x))
        if abs(dx) < eps : return x
    print('seem not convergent')
    return None

a = [4,0,7,1,9,0,0,8]
x = LG(a)
print('{:1.6f}'.format(x))
print(x)
