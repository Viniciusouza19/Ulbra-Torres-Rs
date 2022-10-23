
import funcoes
import os
channels = {'4':0,'5':0,'7':0,'12':0}
channelsValeu = 0
notValid = ''
print('Pesquisa de Audiência de TV')
while True:
    os .system('clear') == None
    print('Canais: 4-Rede Ulbra, 5-Rede Gremeio, 7-Bolso Tv, 12-Lula Flix')
    print(f'{notValid}')
    channel = int(input('Digite o numero do canal ou zero para sair: '))
    
    if channel == 0:
        for key,value in channels.items():
            if value != 0:
                channelsValeu += value
        break
    if channel == 4 or channel == 5 or channel == 7 or channel == 12:
        notValid = ''
        spectators = int(input('Digite a quantidade de espectadores: '))
    else:
        notValid = 'Digite um canal valido!'
        continue
    for key, value in channels.items():
        if str(channel) == key:
            channels[key] = value + spectators

os .system('clear') == None
for i in channels:
    if channels[i] != 0:
        print(f'\n{funcoes.args(int(i))}: teve {channels[i]} espectadores, o que representa {round((channels[i]*100)/channelsValeu)}% do total de espectadores')