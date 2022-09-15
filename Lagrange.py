import numpy as np
import sympy as sy

t = sy.symbols('t')
y = sy.IndexedBase('y')

def  L(n) :
    p = 1
    for i in range (n) : p *= (t-x[i])
    f = 0
    for i in range (n) :
        num = p / (t-x[i])
        den = num.subs(t,x[i])
        f += y[i] * num / den
    return f

a = 0.285
h = 0.1
n = 5
x = np.array([a+i*h  for i in range (n)])

p = L(n)
dp = sy.diff(p,t)

for i in range (n) :
    print('df(x[%d]) =' %i , dp.subs(t,x[i]))
