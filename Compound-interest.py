import math
P	=	float(input("Initial principal balance:"))
r	=	float(input("Interest rate:"))
n	=	float(input("Time periods:"))

rate = (1+ r/100)**(n)
ci = P* rate - P
print("The compound interest is", ci)