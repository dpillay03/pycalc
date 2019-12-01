def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

print('Welcome to PyCalc!')
print('Select an option below:')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')

operation = input("Enter choice(1/2/3/4): ")
x = input('number 1:')
y = input('number 2:')

if operation == 1:
    print('Addition equation=', addition(x,y))
elif operation == 2:
    print('Subraction equation=', subtraction(x,y))
elif operation == 3:
    print('Multiplication Answer=', multiplication(x,y))
elif operation == 4:
    print('Division Answer=', division(x,y))
else:
    print('Invalid input')