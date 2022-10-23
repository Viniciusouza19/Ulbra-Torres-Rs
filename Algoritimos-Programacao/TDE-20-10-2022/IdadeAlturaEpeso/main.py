import json
import IdadeAlturaEpeso.funcoes as funcoes
import time
def data_registration():
    cont = 0
    personal_data = {}
    while True:
        cont = cont + 1
        print('\nInformacoes da pessoa numero:', cont, '\n')
        name = input('Nome: ').capitalize()
        years = int(input(f'Digite a idade de {name}: '))
        height = float(input(f'Digite a altura de {name}: ').replace(',', '.'))
        weight = float((input(f'Digite o peso de {name}: ')).replace(',', '.'))
        personal_data[cont] = {'name': name, 'years': years,
                         'height': height, 'weight': weight}
        if cont == 25:
            break
    with open('IdadeAlturaEpeso/personal_data.json', 'w') as file:
        json.dump(personal_data, file)
data_registration()
time.sleep(2)
print(f'\n{funcoes.mediaAltura_entre10_20()}\n\n{funcoes.amount_of_people()}\n\n{funcoes.calc_weight()}')