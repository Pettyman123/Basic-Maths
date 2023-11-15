a = int(input("Enter the number of values:"))

b=[]
for i in range (0,a):
    c= int(input("enter the number"))
    b.append(c)
    
print(b)
sum = sum(b)

print("The average is",sum/a)