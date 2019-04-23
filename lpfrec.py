import numpy as np
import matplotlib. pyplot as plt
import cmath as cm

wc=np.pi/4				#sinc function

n0=np.arange(-100,100,1)
h0=0.25*np.sinc(0.25*n)

n=np.arange(-17,17,1)
h=0.25*np.sinc(0.25*n)

m=31                                           		#window creation
k=np.arange(0,m)
w=[]		
for i in range(m):
	w=np.append(w,1)

hw=[]					#sinc X window
for i in range(m):
	p=h[i]*1
	hw=np.append(hw,p)
              
def dtft(x):				#lpf
	j=cm.sqrt(-1)
	y=[ ]
	N=10000
	n=len(x)
	p=np.linspace(-np.pi,np.pi,N)
	for i in range(0,N):
		w=p[i]
		sum=0
		for k in range(0,n):
			sum=sum+(x[k]*np.exp(-j*w*k))
		y.append(abs(sum))
	return y
z=dtft(h)

N=10000
n1=np.linspace(-np.pi,np.pi,N)
t=dtft(hw)


plt.subplot(4,1,1)
plt.stem(n,h)
plt.subplot(4,1,2)
plt.stem(k,w)
plt.subplot(4,1,3)
plt.stem(k,hw)
plt.subplot(4,1,4)
plt.plot(n1,t)
plt.show()





	

