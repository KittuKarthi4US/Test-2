def add():
    addition = a + b
    return addition

def subtract():
    subtraction = a - b
    return subtraction

def divide():
    division = a / b
    return division

def multiply():
    multiplication = a * b
    return multiplication

operation = input('Would you like to add, multiply, divide, or subtract :')
if operation != add != multiply != divide != subtract:
    print('Error, Please type it in again')
else:
    pass

if operation == add:
    a = int(input('Enter a number :'))
    b = int(input('Enter a number :'))
print(add)