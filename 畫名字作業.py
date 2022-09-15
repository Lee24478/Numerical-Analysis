import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0,1,100)
def BC(t) :
    b = u0+u1+2*(x0-x1)
    a = x1-x0-u0
    x = x0 + t*(u0+t*(a-b+t*b))
    d = v0+v1+2*(y0-y1)
    c = y1-y0-v0
    y = y0 + t*(v0+t*(c-d+t*d))
    return x,y

fn = input('Enter your filename:')
fo = open(fn)
s = fo.read()
fo.close()
a = s.split()

b = [ eval(a[i]) for i in range (len(a)) ]

n = (len(b))/8
for i in range (int(n)) :
    x0,y0,x1,y1,u0,u1,v0,v1 = b[8*i:8*(i+1)]
    x,y = BC(t)
    plt.plot(x,y,'seagreen')

plt.axis('scaled')
plt.show()
