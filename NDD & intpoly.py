import sympy as sy
t = sy.Symbol('t')

def NDD(x,y) :
    n = len(x)
    for j in range(1,n) :
        for i in range (n-1,j-1,-1) :
            y[i] = (y[i]-y[i-1])/(x[i]-x[i-j])
    return y


x = [1,2,3]
y = [7,-2,9]
f = y.copy()
NDD(x,f)
print(y,f)


def intpoly(x,f) :
    n = len(x)
    p = f[n-1]
    for i in range (n-2,-1,-1) :
        p = f[i] + (t-x[i])*p
    return p

p = intpoly(x,f)
print(p)


