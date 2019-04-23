import numpy as np


x=input("enter the sequence")
h=input("enter the sequence")


m=np.size(x)
n=np.size(h)

k=m+n-1

y=np.zeros(k)

for i in range(m):
	     for j in range(n):
                              y[i+j]=y[i+j]+x[i]*y[j]
	     

print y