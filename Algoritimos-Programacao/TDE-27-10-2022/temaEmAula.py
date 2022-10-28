def questao1():
    n1 = int(input('Digite um numero: '))
    if n1 == 0:
        print('O numero é igual a zero')
    elif n1 > 0:
        print('O numero é positivo')
    elif n1 < 0:
        print('O numero é negativo')


def questao2():
    number1 = int(input("Digite um numero"))

    number2 = int(input("Digite outro numero"))

    number3 = int(input("Digite outro numero"))

    if number1 > number2 and number1 > number3:
        print('O maior numero é: ', number1)

    elif number2 > number1 and number2 > number3:
        print('O maior numero é: ', number2)

    elif number3 > number1 and number3 > number2:
        print('O maior numero é: ', number3)

    def questao2_0():
        number = []
        number.append(int(input("Digite um numero")))
        number.append(int(input("Digite outro numero")))
        number.append(int(input("Digite outro numero")))
        print(f'O maior numeo é: {sorted(number)[-1]}')


def questao3():
    n1 = int(input("Digite um numero"))
    n2 = int(input("Digite outro numero"))
    n3 = int(input("Digite outro numero"))
    if n1 < n2 and n1 < n3:
        print('A soma dos maiores numeros é: ', n2+n3)
    elif n2 < n1 and n2 < n3:
        print('A soma dos maiores numeros é: ', n1+n3)
    elif n3 < n1 and n3 < n2:
        print('A soma dos maiores numeros é: ', n1+n2)


def questao4():
    number = []
    number.append(int(input("Digite um numero")))
    number.append(int(input("Digite outro numero")))
    number.append(int(input("Digite outro numero")))
    print(f'Os numeros em ordem crescente é: {sorted(number)}')

    def questao4_1():
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite outro numero: '))
        n3 = int(input('Digite outro numero: '))
        if n1 > n2 and n1 > n3:  # n1 é o maior
            if n2 > n3:
                print(n3, n2, n1)
            elif n3 > n2:
                print(n2, n3, n1)
        elif n2 > n1 and n2 > n3:  # n2 é o maior
            if n1 > n3:
                print(n3, n1, n2)
            elif n3 > n1:
                print(n1, n3, n2)
        elif n3 > n1 and n3 > n2:  # n3 é o maior
            if n1 > n2:
                print(n2, n1, n3)
            elif n2 > n1:
                print(n1, n2, n3)


def questao5():
    n1 = int(input("Digite um numero"))
    n2 = int(input("Digite outro numero"))
    if n1 == n2:
        print('Os numeros são iguais')
    elif n1 > n2:
        print('O primeiro numero é maior que o segundo')
    elif n2 > n1:
        print('O segundo numero é maior que o primeiro')


def questao6():
    while True:
        user = input('Digite seu usuario: ')
        if user == '1234':
            password = input('Digite sua senha: ')
            if password == '9999':
                print('Autorizado com sucesso')
                break
            else:
                print('Senha incorreta')

        elif user == '0':
            break
        else:
            print('Usuario incorreto')
