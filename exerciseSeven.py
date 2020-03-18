# Exercise Seven (if, elif and else)

# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

symbol = input('Enter one of the symbols +, -, *, / or f(for celsius to fahrenheit conversion): ')
num1 = float(input('Enter a number: '))

if symbol.lower() == 'f':
    print(f'{num1} degrees celsius is equivalent to {num1*(9/5) + 32} degrees fahrenheit!')
else:
    num2 = float(input('Enter another number: ')) 
    if symbol == '+':
        print(num1 + num2)
    elif symbol == '-':
        print(num1 - num2)
    elif symbol == '*':
        print(num1 * num2)
    elif symbol == '/':
        print(num1 / num2)
    else:
        print('Input Error!')