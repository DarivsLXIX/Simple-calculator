
while True:
    num1 = float(input('Enter a number:'))
    operator = input('Enter a operator (+, -, *, /) or q to quit:')
    if operator == 'q':
        break
    num2 = float(input('Enter another number:'))
    if operator == '+':
        print(num1 + num2)
    elif operator == '-':
        print(num1 - num2)
    elif operator == '*':
        print(num1 * num2)
    elif operator == '/':
        print(num1 / num2)