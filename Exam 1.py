import numpy as np 

def rootsearch(f,a,b,dx) :
    x1=a ; f1=f(x1)
    x2=x1+dx ; f2=f(x2)
    while f1*f2>0 :
        if a>=b: return None , None
        x1=x2 ; f1=f2
        x2=x1+dx ; f2=f(x2)
    return x1 , x2


a=0
b=3
dx=0.00001
eps=1.0e-7

f=lambda x: x-2


x1 , x2=rootsearch(f,a,b,dx)
print('%1.4f' %x1,'%1.4f' %x2)


def bc(f,a,b,eps):
    while abs(a-b)>eps :
        t=(a+b)/2
        #print ('%1.4f' %t)
        if f(a)*f(t)<0 : b=t
        elif f(t)*f(b)<0 : a=t
        else: return t 
    return t

t=bc(f,a,b,1.0e-7)
print ('%1.4f' %t)




        
        
        
