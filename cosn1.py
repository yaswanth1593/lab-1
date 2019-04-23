import  numpy as np
import  matplotlib.pyplot as plt

t=np.arange(0,8,0.1)
x1=np.cos(2*np.pi*t)
plt.stem(t,x1)
plt.title("cos wave in discrete domain")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.show()
