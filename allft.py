import numpy as np

from matplotlib import pyplot as plt
import cmath as cm

x=input('entter seq1=')
def dtft(x):
	j=cm.sqrt(-1)
	y=[ ]
	N=14
	n=len(x)
	p=np.linspace(0,2*np.pi,N)
	for i in range(0,N):
		w=p[i]
		print w
		sum=0
		for k in range(0,n):
			sum=sum+(x[k]*np.exp(-j*w*k))
		y.append(abs(sum))
	return y
	

t=dtft(x)

def dft(x):
	j=cm.sqrt(-1)
	y=[ ]
	N=len(x)
	for k in range(0,N):
		w=((2*np.pi)/N)
		sum=0
		for n in range(0,N):
			sum=sum+(x[n]*np.exp(-j*w*k*n))
		y.append(abs(sum))            		          #y.append((sum)) 
	return y

t1=dft(x)
subplot(1,1,1)
plt.plot(x)
subplot(1,2,2)
plt.plot(t)
subplot(2,1,1)
plt.plot(t1)
subplot(2,2,2)
plt.plot(t)

