def factorial():
    fact =  1
    num = int(input("Enter the number to get its factorial"))
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num + 1):
             fact = fact*i
        print("The factorial of",num,"is",fact)

factorial()