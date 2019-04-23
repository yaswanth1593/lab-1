import numpy as np
import matplotlib. pyplot as plt
import cmath as cm

wc=np.pi/4				#sinc function

n0=np.arange(-100,100,1)
h0=0.25*np.sinc(0.25*n0)

n=np.arange(-17,17,1)
h=0.25*np.sinc(0.25*n)

m=31                                           		#window creation
k=np.arange(0,m)
a=(m-1)/2.0
b=np.abs(k-a)
c=2.0*b
d=c/(m-1)
w=1.0-d

hw=[]					#sinc X window
for i in range(m):
	p=h[i]*w[i]
	hw=np.append(hw,p)
              
def dtft(x):				
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
wd=dtft(w)
wdl=20*np.log(wd)
hwd=dtft(hw)
hwdl=20*np.log(hwd)
def dtft(x):				
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
			#z1=np.arctan((np.imag(sum))/(np.real(sum)))
			z1=cm.phase(sum)
		y.append(z1)
	return y
wp=dtft(h)
n1=np.linspace(-np.pi,np.pi,10000)


plt.subplot(5,1,1)
plt.plot(n1,wd)
plt.subplot(5,1,2)
plt.plot(n1,wdl)
plt.subplot(5,1,3)
plt.plot(n1,hwd)
plt.subplot(5,1,4)
plt.plot(n1,hwdl)
plt.subplot(5,1,5)
plt.plot(n1,wp)
plt.show()





	

