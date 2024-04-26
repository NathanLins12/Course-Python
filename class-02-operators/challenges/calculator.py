num1 = input("Digite um número: ")
num2 = input("Digite um número: ")

add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

print(f'''
    {num1} + {num2} = {add}
    {num1} - {num2} = {sub}
    {num1} * {num2} = {mul}
    {num1} / {num2} = {div:.3f}
''')