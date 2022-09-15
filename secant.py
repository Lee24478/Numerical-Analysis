import numpy as np

def sc(f,a,b) :
    eps = 1.0e-7
    while abs(b-a) > eps :
        m = (f(b)-f(a))/(b-a)
        if abs(m) < eps : print("m is too small")
        t = a-f(a)/m
        print(t)
        if f(a)*f(t) < 0 : b=t
        elif f(t)*f(b)  < 0 : a=t
        if abs(f(t)) < eps : break
    return t

a = 1/np.sqrt(5)
b = np.pi
f = lambda x : 9*(np.log(x))+x**3

t=sc(f,a,b)
print(t)
            
