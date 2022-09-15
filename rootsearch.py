import numpy as np 

def rootsearch(f,a,b,dx) :
    x1=a ; f1=f(x1)
    x2=x1+dx ; f2=f(x2)
    while f1*f2>0 :
        if a>=b: return None , None
        x1=x2 ; f1=f2
        x2=x1+dx ; f2=f(x2)
    return x1 , x2

a = 1/np.sqrt(5)
b = np.pi
dx=0.001

f = lambda x : 9*(np.log(x))+x**3

x1 , x2=rootsearch(f,a,b,dx)
print('%1.4f' %x1,'%1.4f' %x2)
