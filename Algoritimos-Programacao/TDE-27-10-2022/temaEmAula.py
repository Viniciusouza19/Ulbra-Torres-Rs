def questao1():
    n1 = int(input('Digite um numero: '))   #recebe o primeiro numero
    
    if n1 == 0:                             #se o numero for igual a 0
        print('O numero é igual a zero')    #imprime que o numero é igual a zero
        
    elif n1 > 0:                            #se o numero for maior que 0
        print('O numero é positivo')        #imprime que o numero é positivo
        
    elif n1 < 0:                            #se o numero for menor que 0
        print('O numero é negativo')        #imprime que o numero é negativo


def questao2():
    number1 = int(input("Digite um numero"))        #recebe o primeiro numero

    number2 = int(input("Digite outro numero"))     #recebe o segundo numero

    number3 = int(input("Digite outro numero"))     #recebe o terceiro numero

    if number1 > number2 and number1 > number3:     #se o primeiro numero for maior que os outros dois numeros
        print('O maior numero é: ', number1)        #imprime o primeiro numero

    elif number2 > number1 and number2 > number3:   #se o segundo numero for maior que os outros dois numeros
        print('O maior numero é: ', number2)        #imprime o segundo numero

    elif number3 > number1 and number3 > number2:   #se o terceiro numero for maior que os outros dois numeros
        print('O maior numero é: ', number3)        #imprime o terceiro numero

    def questao2_0():
        number = [] #cria uma lista vazia
        number.append(int(input("Digite um numero")))      #adiciona o numero digitado na lista
        number.append(int(input("Digite outro numero")))   #adiciona outro numero digitado na lista 
        number.append(int(input("Digite mais um numero"))) #adiciona mais um numero digitado na lista
        print(f'O maior numeo é: {sorted(number)[-1]}')    #imprime o maior numero da lista #sorted ordena a lista em ordem crescente e [-1] pega o ultimo numero da lista mas tbm pode ser usado max(number) que pega o maior numero da lista


def questao3():
    n1 = int(input("Digite um numero"))
    n2 = int(input("Digite outro numero"))
    n3 = int(input("Digite outro numero"))
    if n1 < n2 and n1 < n3:                              # n1 é o menor
        print('A soma dos maiores numeros é: ', n2+n3)   # soma os dois maiores numeros que são n2 e n3
    elif n2 < n1 and n2 < n3:                            # n2 é o menor
        print('A soma dos maiores numeros é: ', n1+n3)   # soma os dois maiores numeros que são n1 e n3
    elif n3 < n1 and n3 < n2:                            # n3 é o menor
        print('A soma dos maiores numeros é: ', n1+n2)   # soma os dois maiores numeros que são n1 e n2


def questao4():
    number = []                                                   #cria uma lista vazia
    number.append(int(input("Digite um numero")))                 #adiciona o numero digitado na lista
    number.append(int(input("Digite outro numero")))              #adiciona outro numero digitado na lista
    number.append(int(input("Digite outro numero")))              #adiciona mais um numero digitado na lista
    print(f'Os numeros em ordem crescente é: {sorted(number)}')   #imprime a lista em ordem crescente #sorted ordena a lista em ordem crescente

    def questao4_1():
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite outro numero: '))
        n3 = int(input('Digite outro numero: '))
        if n1 > n2 and n1 > n3:      # n1 é o maior
            
            if n2 > n3:              # n2 é o segundo maior 
                print(n3, n2, n1)    # n3 é o menor
                
            elif n3 > n2:            # n3 é o segundo maior
                print(n2, n3, n1)    # n2 é o menor
                
        elif n2 > n1 and n2 > n3:    # n2 é o maior
            
            if n1 > n3:              # n1 é o segundo maior
                print(n3, n1, n2)    # n3 é o menor
                
            elif n3 > n1:            # n3 é o segundo maior
                print(n1, n3, n2)    # n1 é o menor
                
        elif n3 > n1 and n3 > n2:    # n3 é o maior
            
            if n1 > n2:              # n1 é o segundo maior
                print(n2, n1, n3)    # n2 é o menor
                
            elif n2 > n1:            # n2 é o segundo maior
                print(n1, n2, n3)    # n1 é o menor


def questao5():
    n1 = int(input("Digite um numero"))                     #recebe o primeiro numero
    n2 = int(input("Digite outro numero"))                  #recebe o segundo numero
    
    if n1 == n2:                                            #se os numeros forem iguais
        print('Os numeros são iguais')                      #imprime que os numeros são iguais
        
    elif n1 > n2:                                           #se o primeiro numero for maior que o segundo numero
        print('O primeiro numero é maior que o segundo')    #imprime que o primeiro numero é maior que o segundo
        
    elif n2 > n1:                                           #se o segundo numero for maior que o primeiro numero
        print('O segundo numero é maior que o primeiro')    #imprime que o segundo numero é maior que o primeiro


def questao6():
    while True:                                            #loop infinito
        
        user = input('Digite seu usuario: ')               #recebe o usuario
        
        if user == '1234':                                #se o usuario for igual a 1234 
            password = input('Digite sua senha: ')        #recebe a senha
            
            if password == '9999':                        #se a senha for igual a 9999
                print('Login realizado')                  #imprime que o login foi realizado
                break                                     #para o loop
            
            else:                                         #se a senha for diferente de 9999
                print('Senha incorreta')                  #imprime que a senha está incorreta

        elif user == '0':                                 #se o usuario for igual a 0
            break                                         #para o loop
        
        else:                                             #se o usuario for diferente de 1234 e 0
            print('Usuario incorreto')                    #imprime que o usuario está incorreto
