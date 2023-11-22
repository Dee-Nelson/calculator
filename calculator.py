

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Insert an operation (+,-,*,/) --->")

add = num1 + num2
subtract = num1 - num2
multiply = num1 * num2
division = num1 / num2

if operation == '+':
    print(add)

elif operation == '-':
    print(subtract)

elif operation == '*':
    print(multiply)

elif operation == '/':
    print(division)

else:
    print("invalid input: try again with operation")



