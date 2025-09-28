# welcome to calculator
print("Welcome to my Calculator")

#select input
num1 = int(input("Enter first number: "))
oprator = input("Enter operator")
num2 = int(input("Enter second number: "))

#logic
if oprator == '+':
    value = num1 + num2
elif oprator == '-':
    value = num1 - num2
elif oprator == '*':
    value = num1 * num2
elif oprator == '/': #zero division error
    if num2 != 0:
        value = num1 / num2
    else:
        value = "cannot divide by zero"
else:
    value = "invalid oprator"
print(value)



