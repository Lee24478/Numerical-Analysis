import numpy as np

def polyfit (x,y,m) :
    n = len(x)
    A = np.zeros((m+1,m+1))
    b = np.zeros(m+1)
    for i in range (m+1) :
        b[i] = np.sum(x**i*y)
        for j in range (m+1) :
            A[i,j] = np.sum(x**(i+j))
    cf = np.linalg.solve(A,b)
    return cf

def eva(x):
    global cf
    m = len(cf) - 1
    f = cf[m]
    for i in range (m-1,-1,-1) :
        f = cf[i] + x*f
    return f

def std(m) :
    global x,y,eva
    return np.sqrt(np.sum( ( y - eva(x) )**2 ) / (len(x)-1-m) )

x = np.array( [1.0,         2.5,      3.5,        4.0,       1.1,     1.8,      2.2,       3.7])
y = np.array([6.008, 15.722, 27.130, 33.772, 5.257, 9.549, 11.098, 28.828])
n = len(x) - 1
for m in range (1,n) :
    cf = polyfit(x,y,m)
    print(np.round(cf,4))
    print ('m=%d,' % m , 'std=%1.4f' % std(m))

