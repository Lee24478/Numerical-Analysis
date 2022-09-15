import numpy as np
import matplotlib.pyplot as plt

def BC(x0,y0,x1,y1,u0,u1,v0,v1) :
    t = np.linspace(0,1,100)
    b = u0+u1+2*(x0-x1)
    a = x1-x0-u0
    x = x0 + t*(u0+t*(a-b+t*b))
    d = v0+v1+2*(y0-y1)
    c = y1-y0-v0
    y = y0 + t*(v0+t*(c-d+t*d))
    return x,y

#李
x1,y1 = BC(0 , 5 , -4 , 4 , -1 , -2 , -1 , -2)
plt.plot(x1,y1,'seagreen')
x2,y2 = BC(-1.5 , 6.3 , -1.5 , 2 , 0.7 , -1 , -0.3 , 1)
plt.plot(x2,y2,'seagreen')
x2_1,y2_1 = BC(-1.5 , 2 , -2.28 , 3.24 , -1 , -1 , 1 , 2)
plt.plot(x2_1,y2_1,'seagreen')
x3,y3 = BC(-1.3 , 4.68 , -5.5 , 1 , 0 , -1 , -2 , 3)
plt.plot(x3,y3,'seagreen')
x4,y4 = BC(-1.3 , 4.4 , 1.645 , 2 , 0 , 1 , 1 , 1)
plt.plot(x4,y4,'seagreen')
x5,y5 = BC(-2 , 1.9 , -0.9 , 2.1 , 0 , 1 , 0 , -0.5)
plt.plot(x5,y5,'seagreen')
x6,y6 = BC(-0.9 , 2.1 , -1.1 , 1.2 , 0.4 , -0.4 , -1 , -1)
plt.plot(x6,y6,'seagreen')
x7,y7 = BC(-1.1 , 1.2 , -1 , -1.5 , 2 , -1.6 , 0 , -0.3)
plt.plot(x7,y7,'seagreen')
x8,y8 = BC(-1 , -1.5 , -2.55 , -0.6 , -1.5 , -1 , 0.15 , 2.3)
plt.plot(x8,y8,'seagreen')
x9,y9 = BC(-2.65 , -0.4 , 0 , 0.3 , 1 , 1 , 0 , -0.3)
plt.plot(x9,y9,'seagreen')
#健
x10,y10 = BC(4.6 , 4.48 , 2.8 , 1.85 , 0 , -5 , -0.6 , -5)
plt.plot(x10,y10,'seagreen')
x11,y11 = BC(2.8 , 1.85 , 4.1 , -0.6 , 5 , 0 , 0 , 0)
plt.plot(x11,y11,'seagreen')
x12,y12 = BC(5.89 , 4.17 , 6.2 , 2 , 0.8 , 0 , 0 , 0)
plt.plot(x12,y12,'seagreen')
x13,y13 = BC(6.2 , 2 , 4.37 , -0.18 , 4.5 , 4 , -12 , 3.1)
plt.plot(x13,y13,'seagreen')
x14,y14 = BC(4.07 , 0.65 , 11.5 , -1.5 , 6 , 15 , 1 , 0)
plt.plot(x14,y14,'seagreen')
x15,y15 = BC(6.39 , -0.11 , 9.5 , 1.36 , 1 , 2 , 0 , 2.3)
plt.plot(x15,y15,'seagreen')
x15,y15 = BC(6.51 , 0.45 , 8.09 , 0.45 , 13.8 , -2 , 5 , -2.3)
plt.plot(x15,y15,'seagreen')
x15,y15 = BC(8.1 , 6.1 , 8.2 , 0.49 , 1 , 0 , 0 , 15.9)
plt.plot(x15,y15,'seagreen')
x15,y15 = BC(6.8 , 1.55 , 9.45 , 2.15 , 1 , 1 , 0 , 0)
plt.plot(x15,y15,'seagreen')
x15,y15 = BC(6.9 , 5.28 , 8.1 , 2.8 , 1 , -14 , -2.5 , -11)
plt.plot(x15,y15,'seagreen')
x15,y15 = BC(6.62 , 3.4 , 10.1 , 3.3 , 1 , 1 , -2.5 , -0.3)
plt.plot(x15,y15,'seagreen')
#立
x15,y15 = BC(16.5, 6.11 , 16.55 , 4 , 2.5 , -1 , 0 , -0.3)
plt.plot(x15,y15,'seagreen')
x15,y15 = BC(14.66 , 2.89 , 18.7 , 3.88 , 1 , 1 , 0.3 , 1)
plt.plot(x15,y15,'seagreen')
x15,y15 = BC(14.76 , 3.1 , 15.66 , 0.19 , 0 , 2 , -10 , 1)
plt.plot(x15,y15,'seagreen')
x15,y15 = BC(15.66 , 0.19 , 18.76 , 3.07 , 2 , 0 , 1 , -3)
plt.plot(x15,y15,'seagreen')
x15,y15 = BC(18.76 , 3.07 , 15.08 , -1.3 , 1 , -6 , -7 , -1)
plt.plot(x15,y15,'seagreen')
x15,y15 = BC(12.21 , -0.8 , 21.67 , -1.5 , 2 , 5 , -8 , -8)
plt.plot(x15,y15,'seagreen')


plt.axis('scaled')
plt.show()


