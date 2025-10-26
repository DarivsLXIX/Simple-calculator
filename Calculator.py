num1 = input('Enter a number:')
num2 = input('Enter another number:')
print('Enter your operation:')
op = input()

try:
    if op == '+':
        print(int(num1) + int(num2))
    elif op == '-':
        print(int(num1) - int(num2))
    elif op == '*':
        print(int(num1) * int(num2))
    elif op == '/':
        print(int(num1) / int(num2))
    else:
        print('Invalid operation.')
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid numbers.")
input("Press Enter to exit...")