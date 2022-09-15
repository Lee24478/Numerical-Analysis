import numpy as np

def evalpoly(a,x) :
    n = len(a)-1
    p = a[n]
    dp = 0.0+0.0j
    ddp = 0.0+0.0j
    for i in range (1,n+1) :
        ddp = 2.0*dp + x*ddp
        dp = p + x*dp
        p = a[n-i] + x*p
    return p,dp,ddp

a = [1,1,1]  # x**2 + x + 1
x = 1  # 帶入方程式

p,dp,ddp = evalpoly(a,x)
print(p,dp,ddp)
        
