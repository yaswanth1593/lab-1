a=input("enter the number")
b=input("enter the number")
c=input("enter the number")
if(a>b and a>c):
	if(b>c):
		print c,b,a
	else:
		print b,c,a
if(b>a and b>c):
	if(a>c):
		print c,a,b
	else:
		print a,c,b
if(c>a and c>b):
	if(a>b):
		print b,a,c
	else:
		print a,b,c
