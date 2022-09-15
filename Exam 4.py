import numpy as np
import sympy as sy
t = sy.Symbol('t')

def NDD(x,y) :
    n = len(x)
    for j in range (1,n) :
        for i in range (n-1,j-1,-1) :
            y[i] = (y[i]-y[i-1])/(x[i]-x[i-j])
    return y

x = [1,2,3]
y = [7,8,11]
f = NDD(x,y)
print(f)

def intpoly(x,f) :
    n = len(x)
    p = f[n-1]
    for i in range (n-2,-1,-1) :
        p = f[i] + (t-x[i])*p
    return p

p = intpoly(x,f)
print(p)
b = sy.expand(p)
print(b)

fp = np.polynomial.Polynomial([0])
n = len(f)
for i in range (n) :
    s = np.polynomial.Polynomial([1])
    for j in range (i) :
        s_temp = np.polynomial.Polynomial([-x[j],1])
        s = np.polymul(s_temp,s)
    s *= f[i]
    fp = np.polyadd(fp,s)

d = fp[0].coef
print(d)

