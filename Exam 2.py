import numpy as np

def secant(f,a,b) :
    eps=1.0e-7
    while abs(b-a) > eps :
        m = (f(b)-f(a))/(b-a)
        if abs(m) < eps : print('m is too small')
        t = a-f(a)/m
        #print(t)
        if f(a)*f(t) < 0 : b=t
        elif f(t)*f(b) < 0 : a=t
        if abs(f(t)) < eps : break
    return t

def ridder(f,a,b) :
    x1 = a ; f1 = f(x1)
    x2 = b ; f2 = f(x2)
    eps = 1.0e-7
    while abs(x1-x2) > eps :
        x3 = (x1+x2)/2 ; f3 = f(x3)
        s = np.sqrt(f3**2-f1*f2)  #背
        e1 = (f3 + s)/f2 ; e2 = (f3 - s)/f2  #背
        if e1 < 0 : E = e2
        else : E = e1
        q = f3*E*(x3-x1)/(f3*E-f1)  #背
        x4 = x3-q ; f4 = f(x4)
        #print(x4)
        if x4 < x3 :
            if f1*f4 < 0 :
                x2 = x4 ; f2 = f4
            else :
                x1 = x4 ; f1 = f4
                x2 = x3 ; f2 = f3
        else :
            if f3*f4 < 0 :
                x1 = x3 ; f1 = f3
                x2 = x4 ; f2 = f4
            else :
                x1 = x4 ; f1 = f4
    return x4 , f4

        
a=1/np.sqrt(5)
b=np.pi
f = lambda x : 9*(np.log(x))+x**3

t = secant(f,a,b)
t1,t2= ridder(f,a,b)
print('ridder:',t1,"v.s" ,'secant:',t)
    
