print("Hello world!")
num1=input("Enter first number: ")
num2=input("Enter second number: ")
operation=input("Enter operation: ")
if operation.lower() == "x":
    operation="*"
print(eval(num1+operation+num2))
