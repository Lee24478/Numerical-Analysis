import numpy as np

def SynDiv(a,b) :  # a 是降冪排列 
    n = len(a)-1
    for i in range (1,n+1) :
         a[n-i] += a[n-i+1]*b


a = [5,4,3,2,1]   # 5+4x+3(x^2)+2(x^3)+(x^4)
b = 2   # 除以(x-2)
SynDiv(a,b)
print(a)



