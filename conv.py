import numpy as np
def  convolution(A,B):       

	lengthA=np.size(A)   
	lengthB=np.size(B)   
    
	C = np.zeros(lengthA+ lengthB-1)        


	for m in np.arange( lengthA ):       
   	       for n in np.arange(lengthB):            
                           C[m+n] = C[m+n] + A[m]*B[n]                          
	return  C 




x=input("enter the sequence")
h=input("enter the sequence")


t=convolution(x,h)

print t