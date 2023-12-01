a = int(input("Enter the cost you bought at:"))
b = int(input("Enter the cost you sold:"))

x= (b-a)/a

if x>0:
    print("It was a profit  by",x*100,"% percent")
else:
    print("It was loss by",x*100*(-1),"% percent")