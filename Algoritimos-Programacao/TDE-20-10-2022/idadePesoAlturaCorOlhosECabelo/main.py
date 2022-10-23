import json
import funcoes
import time
def data_registration():
    cont = 0
    data_base = {}
    while True:
        cont = cont + 1
        print('\nInformacoes da pessoa numero:', cont, '\n')
        years = int(input(f'Digite a idade: '))
        height = float(input(f'Digite a altura: ').replace(',', '.'))
        weight = float((input(f'Digite o peso: ')).replace(',', '.')) 
        eyes_color = input(f'\nDigite uma das cores dos olhos:\nA-azul, V-verde, C-castanho, P-preto\nDigite a opcao: ').upper()
        hair_colors = input(f'\nDigite uma das cores dos cabelos:\nL-loiro, P-preto, C-castanho, R-ruivo\nDigite a opcao: ').upper()
        data_base[cont] = {'idade': years, 'altura': height, 'peso': weight, 'cor dos olhos': funcoes.eyes_colors(eyes_color), 'cor dos cabelos': funcoes.hair_colors(hair_colors)}
        if cont == 25:
            break
    with open('idadePesoAlturaCorOlhosECabelo/dados.json', 'w') as file:
        json.dump(data_base, file)
data_registration()
time.sleep(1)
funcoes.years()
funcoes.height()
funcoes.blue_eyes()
funcoes.hair_colors_ruivo_Blue_eyes()