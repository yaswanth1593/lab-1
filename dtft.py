import numpy as np

from matplotlib import pyplot as plt
import cmath as cm


def dtft(x):
	j=cm.sqrt(-1)
	y=[ ]
	for w in np.linspace(-2,2,0.1):
		sum=0
		for n in range(0,len(x),1):
			sum=sum+x[n]*np.exp(-j*w*n)
		y=np.append(y,abs(sum))
	return y
	
	


        

x=input('entter seq1=')
k=np.linspace(-2,2,0.1)
t=dtft(x)
plt.plot(k,t)
plt.show()




