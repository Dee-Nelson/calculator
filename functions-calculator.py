def add(x, y):
    ans = x + y
    return ans


def sub(x, y):
    ans = x - y
    return ans


def mult(x, y):
    ans = x * y
    return ans


def div(x, y):
    ans = x / y
    return ans


x = float(input("ENTER THE FIRST DIGIT:   "))
y = float(input("ENTER THE SECOND NUMBER:    "))
operation = input("choose operand (+,-,/,*):   ")

if operation == "+":
    print(add(x,y))

elif operation == "-":
    print(sub(x, y))

elif operation == "*":
    print(mult(x, y))

elif operation == "/":
    print(div(x, y))

else:
    print('Invalid entry: enter an operand')
