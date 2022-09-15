import numpy as np

def evalpoly(a,x) :
    n = len(a)-1
    p = a[n]
    dp = 0.0+0.0j
    ddp = 0.0+0.0j
    for i in range (1,n+1) :
        ddp = 2*dp + x*ddp
        dp = p + x*dp
        p = a[n-i] + x*p
    return p,dp,ddp

def Laguerre(a) :  # a是其中一個解
    n = len(a)-1
    eps  = 1.0e-7
    x = np.random.uniform(-9.9,9.9)  #初始值 (這裡隨機給)
    for i in range (30) :
        p,dp,ddp = evalpoly(a,x)
        g = dp/p ; h = g**2-ddp/p  #背
        q = np.sqrt((n-1)*(n*h-g**2))  #背
        if abs (g+q) > abs (g-q) : dx = n/(g+q)
        else : dx = n/(g-q)
        x -= dx
        print('{:1.5f}'.format(x))  #格式化輸出 (小數後5位)
        if abs (dx) < eps : return x
    print('seem not convergent')
    return None

a = [4,0,7,1,9,0,0,8]
x = Laguerre(a)
print('{:1.5f}'.format(x))
print(x)
        
