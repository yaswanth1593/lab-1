import numpy as np
from matplotlib import pyplot as plt

x = input('enter a sequence')
h = input('enter another sequence')
n1=len(x)
n2 = len(h)
n =np.max(n1,n2)
a=np.arange(0,n,1)
x = [x,np.zeros(1,n-n1)]
h = [h,np.zeros(1,n-n2)]

def pconv(n):
      y = np.zeros(1,n)
      l=n-1
      for i in range(0,l):
              for j in rane(0,l):
                       k = np.mod((i-j),n)
                       y(i+1) = y(i+1) + x(j+1)*h(k+1)
      return y

t=pconv(n)            



plt.stem(a,t)
plt.show()