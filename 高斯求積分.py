import numpy as np
import sympy as sy

n = 9
t = sy.symbols('t')
p = sy.Poly( sy.diff((1-t**2)**n,t,n) )
c = p.all_coeffs()
x = np.sort(np.roots(c))

cf = []
for i in range(n):
    L = 1
    for j in range(n):
        if j != i : L *= (t-x[j]) / (x[i]-x[j])
    cf.append( float( sy.integrate(L,(t,-1,1)) ) )

f = lambda u,v : np.log(u**2+v+1)
a = -np.exp(1)
b = 2*np.exp(1)
M = (b+a)/2
R = (b-a)/2
X = R*x+M
c = lambda u : -u
d = lambda u : u**2+2
m = (d(X)+c(X))/2
r = (d(X)-c(X))/2

I = 0
for i in range(n):
    I += R*( cf[i]*r[i]*sum( cf*f(X[i],r[i]*x+m[i]) ) )

print('%1.4f' %R , ' * { ' , end = ' ' )
for i in range(n):
    print( 'c[',i+1,']' , ' * ' , '%1.4f' %r[i] , ' * ' , ' ( %1.4f ) ' %sum( cf*f(X[i],r[i]*x+m[i]) ) , end = ' ' )
    if i != n-1 : print(' + ' , end = ' ')
print('} = %1.4f' %I) 
