a = float(input("Enter the person A cost:"))
b = float(input("Enter the person B cost:"))

ratioA = a/(a+b)
ratioB = 1- ratioA

profit = float(input("Enter the profit:"))

print("Profit for A:", ratioA* profit)

print("Profit for B:", ratioB* profit)