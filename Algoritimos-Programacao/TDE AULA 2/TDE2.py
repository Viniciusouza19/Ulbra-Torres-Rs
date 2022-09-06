import time

def titulo(txt):
    print('-'*len(txt))
    print('\033[34m'+txt+'\033[0;0m')
    print('-'*len(txt))
def printt(txt):
    print('-'*len(txt))
    print(txt)
    print('-'*len(txt))

def limpar():
    try:
        import os
        linhas = os.get_terminal_size().linhas
    except AttributeError:
        linhas = 130
    print("\n" * linhas)

def quest_1():
    limpar()
    titulo('#1. Faça um algoritmo que resolva as seguintes expressões aritméticas considerando A=2,B=5 e C=10. Mostre o resultado na tela da expressão')
    a = 2
    b = 5
    c = 10
    printt(f'O resultado de a. A+B*C/A É: {a+b*c/a}\nO Resultado de b. (A+B)*C/A é: {(a+b)*c/a}\nE o resultado de c. (A+B*C)/A é: {(a+b*c)/a}')
    print('\n\nBy VINICIUS SOUZA')
    input('Tecle ENTER para voltar ao MENU inicial: ')

def quest_2():
    limpar()
    titulo('2. Faça um algoritmo que leia dois números reais e imprima a soma e a média aritméticadesses números.')
    numero1 = float(input('Digite um numero: ').replace(',','.'))
    numero2 = float(input('Digite outro numero: ').replace(',','.'))
    calculo = (numero1+numero2)/2
    printt(f'A soma entre {numero1} e {numero2} é {numero1+numero2:.2f} \nE a Media de {numero1+numero2:.2f} é {calculo:.2f}')
    print('\n\nBy VINICIUS SOUZA')
    input('Tecle ENTER para voltar ao MENU inicial: ')
def quest_3():
    limpar()
    titulo('3. Faça um algoritmo que leia um número inteiro e imprima seu antecessor e seu sucessor.')
    titulo('DIGITE APENAS NUMEROS ESTE CODIGO SO FUNCIONA PARA NUMEROS INTEIROS E N FUNCIONA PARA NUMEROS NEGATIVOS')
    r = 'S'
    while r == 'S':
        try:
            numero = int(input('Digite um numero inteiro: '))
            printt(f'O {numero} tem o antecessor {numero - 1} e o sucessor {numero + 1}')

            r = str(input('Quer fazer novamente [S/N]: '))

        except:
            print('Digite apenas numeros inteiros!!! ')
    print('Muito obrigado por usar esse codigo python BY VINICIUS TEMA ULBRA')


def quest_4():
    limpar()
    titulo('4. Faça um algoritmo para calcular a média aritmética entre três números quaisquer.')
    memoria_dos_numeros = []
    for i in range(3):
        calcuMedia = float(input(f'{i+1}-Digite um numero: '))
        memoria_dos_numeros.append(calcuMedia)
        calculo = sum(memoria_dos_numeros)
    printt(f'A soma entre {memoria_dos_numeros} é {calculo}\nE a media entre os numeros {memoria_dos_numeros} é {calculo/i}')
    print('\n\nBy VINICIUS SOUZA')
    input('Tecle ENTER para voltar ao MENU inicial: ')



def quest_5():
    limpar()
    titulo('5. Faça um algoritmo (FUA) que lê o número de um funcionário, seu número de horas trabalhadas e o valor que recebe por hora. O algoritmo deve calcular e mostrar o salário deste funcionário.')
    r = 's'
    while r == 's':
        numero_funcionario = int(input('Digite o numero do funcionario: ').capitalize())
        time.sleep(0.1)
        horas_trabalhada = float(input(f'Digite o numero de horas Mensais trabalhada pelo funcionario N-{numero_funcionario}: ').replace(',','.'))
        time.sleep(0.1)
        valor_hora = float(input(f'Digite o valor hora do funcionario {numero_funcionario}: ').replace(',','.'))
        time.sleep(0.1)  
        printt(f'O funcionario {numero_funcionario} \nTrabalhou {horas_trabalhada:.2f} horas no mes\n{numero_funcionario} ganha R${valor_hora:.2f} por hora totalizando um salario mensal de R${valor_hora*horas_trabalhada:.2f}')
        time.sleep(0.1)
        r = input('Quer continuar [s/n]: ')
    print('Muito obrigado por usar esse codigo python BY VINICIUS TEMA ULBRA')

def quest_6():
    limpar()
    titulo('6. FUA para ler dois inteiros (variáveis A e B) e efetuar as operações de adição, subtração, multiplicação e divisão de A por B apresentando ao final os quatro resultados obtidos.')
    num1 = int(input('Digite um numero inteiro: '))
    num2 = int(input('Digite outro numero inteiro: '))
    printt(f'Os numeros {num1} e {num2}\nSomados sao {num1+num2}\n{num1} - {num2} = {num1-num2}\n{num1} / {num2} = {num1/num2:.2f}')
    print('\n\nBy VINICIUS SOUZA')
    input('Tecle ENTER para voltar ao MENU inicial: ')



def quest_7():
    limpar()
    titulo('7. FUA para calcular a área de um triângulo, exibindo o resultado. A base e a altura são dados que devem ser lidos como entrada.')
    repetir = 's'

    while repetir == 's':
        try:
            menu = int(input('Digite opçao de calculo: \n[ 1 ] AREA DE UM TRAPEZIO\n[ 2 ] AREA DE UM TRIANGULO\n: '))

            if menu == 1:
                baseMenor = float(input('Digite a base menor de um trapezio: ').replace(',','.'))
                print('')
                baseMaior = float(input('Digite a base maior de um trapezio: ').replace(',','.'))
                print('')
                altura = float(input('Digite a altura do triangulo: ').replace(',','.'))
                print('=*'*25)
                printt(f'A área do trapezio é:',(baseMaior+baseMenor)*altura/baseMenor)
                print('=*'*25)

            elif menu == 2:
                base = float(input('Digite a base do Triangulo: ').replace(',','.'))
                print('')
                altura = float(input('Digite a altura do triangulo: ').replace(',','.'))
                print('=*'*25)
                printt('A área do triãngulo é:', (base*altura)/2)
                print('=*'*25)

        except:
            print('=*'*25)
            print('Digite apenas numeros!!!')
            print('=*'*25)

        repetir = input('Voce quer cotinuar os calculos [s/n]: ')

def quest_8():
    limpar()
    titulo('8. Uma loja de animais precisa de um algoritmo para calcular os custos de criação de coelhos. O custo é calculado com a fórmula CUSTO=(NRO_COELHOS*0.70)/18+10. O algoritmo tem como entrada o número de coelhos, devendo fornecer, como saída, o custo.')
    repetir = 's'
    while repetir == 's':
        try:
            numero_coelhos = int(input('Digite o numero de coelhos para calcular o custo de criaçao: '))
            calculo = (numero_coelhos*0.70)/18+10
            print('')
            printt(f'A quantidade de {numero_coelhos} coelhos teria um custo de criaçao de R${calculo:.2f} ')
        except:
            print('=*'*25)
            print('Digite apenas numeros inteiros pq n tem como ter meio coelho a n ser que ele esteje fatiado!!!')
            print('=*'*25)

        repetir = input('Voce quer cotinuar os calculos [s/n]: ')



def quest_9():
    limpar()
    titulo('9. F.U.A para calcular o valor de lucro que um vendedor tem em um produto, com base em seu preço de custo e o preço de venda.')
    repetir = 's'
    while repetir == 's':
        try:
            custo = float(input('Digite o custo do produto: ').replace(',','.'))
            preco_de_venda = float(input('Digite o preço de venda do produto: ').replace(',','.'))
            calculor_lucro = preco_de_venda-custo
            print('*'*30)
            printt(f'O produto no custo de R${custo:.2f} e com o preço de venda de R${preco_de_venda:.2f}\nTem o lucro de R${calculor_lucro:.2f} e a margen de lucro de {(calculor_lucro/preco_de_venda)*100:.2f}%')
            print('=*'*25)

        
        except:
            print('=*'*25)
            print('Digite apenas numeros!!')
            print('=*'*25)

        repetir = input('Voce quer cotinuar os calculos [s/n]: ')

def quest_10():
    limpar()
    titulo('10.F.U.A que leia o preço de um produto e a quantidade comprada e exiba para o usuário o preço que ele tem que pagar pela compra.')
    repetir = 's'
    while repetir == 's':
        nome_produto = str(input('Digite o nome do produto a ser comprado: '))
        try:
            preço_produto = float(input(f'Qual o valor unitario do {nome_produto} que voce ira comprar R$ ').replace(',',''))
            quantidade_comprada = int(input(f'Qual a quantidade de {nome_produto} que voce ira comprar: '))
            calculor_custo = float(preço_produto*quantidade_comprada)
            print('*'*30)
            printt(f'Na compra de {quantidade_comprada} {nome_produto} voce ira gastar R${calculor_custo:.0f}'.upper())
            print('=*'*25)

      
        except:
            print('=*'*25)
            print('LEIA COM ATENÇAO OQ ESTA SENDO PEDIDO!!')
            print('=*'*25)

        repetir = input('Voce quer cotinuar os calculos [s/n]: ')

def quest_11():
    limpar()
    titulo('11.F.U.A que leia dois números e calcule qual é o resto da divisão do 1o pelo 2o número. Exiba na tela este valor final.')
    num1 = float(input('Digite um numero: '))
    num2 = float(input('Digite outro numero: '))
    resto = num1%num2
    print('\n')
    printt(f'O resto da divisao do numero {num1} % {num2} \nÉ {resto} \nE o resoltado da divisao é {num1/num2}')
    print('By VINICIUS SOUZA')
    input('Tecle ENTER para voltar ao MENU inicial: ')

def quest_12():
    limpar()
    titulo('12. F.U.A que leia dois números e calcule qual é o valor inteiro da divisão do 2o pelo 1o número. Exiba na tela este valor final.')
    num1 = float(input('Digite um numero: '))
    num2 = float(input('Digite outro numero: '))
    resto = num2%num1
    print('\n') 
    printt(f'O resto da divisao do numero {num2} % {num1} \nÉ {resto} \nE o resultado da divisao é {num2/num1}')
    print('By VINICIUS SOUZA')
    input('Tecle ENTER para voltar ao MENU inicial: ')

def main():
    while True:
        try:
            limpar()
            titulo('MENU CRIADO POR VINICIUS DE SOUZA NASCIMENTO ULBRA TORRES 1 SEMESTRE RESPOSTAS PARA EXERCICIOS DO DIA 11/08/2022 PROFESSOR PAULO IGNACIO\nMATERIA ALGORITIMO E LOGICA DE PROGRAMAÇAO ')
            print()
            print('Opções: ')
            print('[ 1 ]-Resposta questao-1  [ 2 ]-Resposta questao-2 ')
            print('[ 3 ]-Resposta questao-3  [ 4 ]-Resposta questao-4 ')
            print('[ 5 ]-Resposta questao-5  [ 6 ]-Resposta questao-6 ')
            print('[ 7 ]-Resposta questao-7  [ 8 ]-Resposta questao-8 ')
            print('[ 9 ]-Resposta questao-9  [ 10 ]-Resposta questao-10 ')
            print('[ 11 ]-Resposta questao-11 [ 12 ]-Resposta questao-12 ')
            print('[ 0 ]-EXIT')

            resp = int(input('Digite sua opçao: '))

            if resp == 1:
                quest_1()
            elif resp == 2:
                quest_2()
            elif resp == 3:
                quest_3()
            elif resp == 4:
                quest_4()
            elif resp == 5:
                quest_5()
            elif resp == 6:
                quest_6()
            elif resp == 7:
                quest_7()
            elif resp == 8:
                quest_8()
            elif resp == 9:
                quest_9()
            elif resp == 10:
                quest_10()
            elif resp == 11:
                quest_11()
            elif resp == 12:
                quest_12()
            
            elif resp == 0:
                break
        except:
            titulo('DIGITE APENAS OPÇOES VALIDAS LOADING!!!')
            time.sleep(3)

main()
