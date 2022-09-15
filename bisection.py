import numpy as np

def bisection(f,a,b,eps):
    while abs(a-b)>eps :
        t=(a+b)/2
        #print ('%1.4f' %t)
        if f(a)*f(t)<0 : b=t
        elif f(t)*f(b)<0 : a=t
        else: return t 
    return t

a = 1/np.sqrt(5)
b = np.pi
f = lambda x : 9*(np.log(x))+x**3

t=bisection(f,a,b,1.0e-7)
print ('%1.8f' %t)
