# Faça um programa que leia um valor inteiro (que representa o real, moeda nacional) e calcule qual o menor número
# possível de reais/moedas de 100, 50, 20, 10, 5, 2 e 1 em que o valor lido pode ser decomposto. Escrever o valor
# lido e a relação de reais necessárias.
import pyautogui

#______funçao para parar
def breaks():
    b = input('Digite 0 para sair ou Enter para continuar: ')
    if b == '0':
        pyautogui.hotkey('ctrl', 'c')

#______funçao da matematica utilizada!!
def troco():
    reais1 = int(input(
        'Quantos reais voce quer decompor: '))
    total = reais1
    reais = 100
    totaln = 0
    while True:
        if total >= reais:
            total -= reais
            totaln += 1
        else:
            if totaln > 0:
                print(f'O total de {totaln} cedulas de R${reais}: ')
            if reais == 100:
                reais = 50
            elif reais == 50:
                reais = 20
            elif reais == 20:
                reais = 10
            elif reais == 10:
                reais = 5
            elif reais == 5:
                reais = 1
            totaln = 0
            if total == 0:
                break
            
#______Repetidor
while True:
    troco()
    breaks()
    
