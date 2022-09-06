def p (txt):
    print('*'*len(txt))
    print(txt)
    print('*'*len(txt))

num1 = float(input('Digite o primeiro numero: ').replace(',','.'))
num2 = float(input('Digite segundo numero: ').replace(',','.'))


#Par ou impar
if (num1%2) == 0:
        p(f"O {num1} Par")
else:
    p(f"O {num1} Ímpar")
    
if (num2%2) == 0:
        p(f"O {num2} é Par")
else:
    p(f"O {num2} Ímpar")
    
#Maior ou menor numero 1 e numero 2
if num1 < 10:
    p(f'O numero {num1} é menor  que 10')
else:
    p(f'O numero {num1} é maior ou igual a 10')
    
if num2 < 10:
    p(f'O numero {num2} é menor  que 10')
else:
    p(f'O numero {num2} é maior ou igual a 10')

#Quadrado, restos e soma
p(f'O quadrado de {num1} é {num1**2:.2f} e o quadrado de {num2} é {num2**2:.2f}')
p(f'O Resto da divisao do {num1} é {num1%2:.2f} E o Resto da divisao do {num2} é {num2%2:.2f}')
p(f'A soma entre {num1} e {num2} é {num1+num2:.2f}')
