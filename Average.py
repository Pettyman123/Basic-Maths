a = int(input("Enter the number of values:"))

b=[] #empty list
for i in range (0,a):
    c= int(input("enter the number"))
    b.append(c)
    
print(b)#The list of all input values
sum = sum(b) #sum function adds all the entites of the list

print("The average is",sum/a)
