import math

print("The polynomail is the format of the ax^2 + bx + c")
a = float(input("Enter the value of a:"))
b = float(input("Enter the value of b:"))
c = float(input("Enter the value of c:"))

x = 'x'
y = 'a(x^2) + bx + c = 0 '
print("The polyonmial u have enetred is", y)
D = b*b - 4*a*c

def roots2():
    x1 = (-b + math.sqrt(D))/(2*a)
    x2 = (-b - math.sqrt(D))/(2*a)
    print("The roots of the polynomial",y, "are", round(x1,3), "and ", round(x2,3))
    
def roots1():
    print(str(-b/2*a) ,"+","i{}".format(math.sqrt(D)/(2*a)))
    print(str(-b/2*a) ,"-","i{}".format(math.sqrt(D)/(2*a)))

#print("The roots of the polynomial",y, "are", x1, "and ", x2)

if D<=0:
    D = (-1)*D
    roots1()   
else:
    D = 1*D
    roots2()

