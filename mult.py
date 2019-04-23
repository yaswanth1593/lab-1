import  numpy as np
import  matplotlib.pyplot as plt

t=np.arange(0,10,0.1)
x1=np.exp(-t)
x2=np.sin(t)
x3=x1*x2
plt.plot(t,x3)
plt.title("log function")
plt.xlabel("time")
plt.ylabel("amplitude")


plt.show()
