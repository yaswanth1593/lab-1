import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt

fs,d8k=wav.read('myvoice.wav')   
print(fs,len(d8k))   
print(d8k) 


fs1,d8kc=wav.read('myvoice16.wav')  
print(fs1,len(d8kc))   
print(d8kc) 

fs2,d8ke=wav.read('myvoice2k.wav')   
print(fs2,len(d8ke))   
print(d8ke) 
                                   
t=np.arange (0,len(d8k)/fs,1.0/fs)
t1=np.arange (0,len(d8kc)/fs1,1.0/fs1)
t2=np.arange (0,len(d8ke)/fs2,1.0/fs2)

plt.subplot(3,1,1)
plt.plot(t,d8k)
 
plt.subplot(3,1,2)
plt.plot(t1,d8kc)

plt.subplot(3,1,3)
plt.plot(t2,d8ke)

plt.show()


