from random import random
from funcoes import pesq_funcionario, imprime_funcionario,input2
import os
import random

#Variaveis
banco_funcionario = {}
comando = "continue"

#Laço
while True:
    try:
        #Opçoes
        os.system('clear') or None
        comando = int(input('Digite a opção desejada: \n1-[Novo-funcionario]\n2-[Pesquisar-funcionario]\n3-[Sair]\nDigite uma das opçoes: '))
        os.system('clear') or None
        
        #Opçao 1 cadastro de funcionario do banco de dados
        if comando == 1:
            
            #Inputs de cadastro
            numero_funcionario = random.randint(10,1000)
            input(f'O numero deste funcionario é {numero_funcionario} tecle ENTER para continuar: ')
            os.system('clear') or None
            nome = input('Digite o nome do funcionario: ').strip().capitalize()
            os.system('clear') or None
            idade_func = input(f"Digite a idade do funcionario {nome} : ").strip()
            os.system('clear') or None
            num_filhos = int(input(f"Quantos filhos o funcionario {nome} tem com idade inferior a 14 anos ? ").strip())
            os.system('clear') or None
            temp_servico = input(f"Quanto Anos de serviço o funcionario {nome} tem: ").strip()
            os.system('clear') or None
            num_hora = float(input(f"Digite as horas trabalhadas mensalmente do funcionario {nome}: ").strip().replace(',','.'))
            os.system('clear') or None
            valor_hora = int(input(f"Digite quanto o funcionario {nome} recebe por hora: ").strip())
            os.system('clear') or None
    
            #Calculo e variaveis de calculo inicio
            salario_bruto = (num_hora*valor_hora)+(200*num_filhos)
            inss = salario_bruto/100*8.5
            
            if salario_bruto > 1500:
                ir = salario_bruto/100*15

            elif salario_bruto > 500 and salario_bruto <= 1500:
                ir = salario_bruto/100*8

            elif salario_bruto <= 500:
                ir = 0
            total_desconto = ir+inss
            salario_liquido = salario_bruto-total_desconto
            #Calculo e variaveis de calculo fim
            
            #Adiçao ao banco de dados 
            banco_funcionario[nome.lower()] ={
                "numero-funcionario": numero_funcionario,
                "nome": f'{nome}'.capitalize(),
                "tempo-servico": f'{temp_servico} anos',
                "salario-familia": f'R${200*num_filhos:.2f}',
                "salario-bruto": f'R${salario_bruto}',
                "total-Desconto": f'R${total_desconto:.2f}',
                "salario-liquido": f'R${salario_liquido}'
            }
        #Opçao 2  Pesquisar funcionario
        elif comando == 2:
            nome = input('Digite o nome do funcionario: ').lower()
            chaves_encontradas = pesq_funcionario(banco_funcionario, nome)
            os.system('clear') or None
            imprime_funcionario(banco_funcionario, chaves_encontradas)
            os.system('clear') or None
            
        #Opçao 3 parar programa
        elif comando == 3:
            break
        
        #Tratamento de erro simples
        else:
            print('Digite apenas caracteres validos leia atentamente!! ')
            
    #Exeçoes
    except:
        print('Digite opçoes validas!!!')