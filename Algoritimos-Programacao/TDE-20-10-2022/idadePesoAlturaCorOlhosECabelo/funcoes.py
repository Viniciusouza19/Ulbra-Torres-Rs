import json
with open ('idadePesoAlturaCorOlhosECabelo/dados.json', 'r') as file:
    data_base = json.load(file)

def hair_colors(resp):
    if resp == 'L':
        return 'Loiro'
    elif resp == 'P':
        return 'Preto'
    elif resp == 'C':
        return 'Castanho'
    elif resp == 'R':
        return 'Ruivo'
    else:
        return 'Cor de cabelo invalida'

def eyes_colors(resp):
    if resp == 'A':
        return 'Azul'
    elif resp == 'V':
        return 'Verde'
    elif resp == 'C':
        return 'Castanho'
    elif resp == 'P':
        return 'Preto'
    else:
        return 'Cor de olhos invalida'

def years():
    years_base = []
    for i in data_base:
        if data_base[i]['idade'] > 50 and data_base[i]['peso'] < 60:
            years_base.append(data_base[i]['idade'])
        if len(years_base) == 0 or len(years_base) == 1:
            resp = ''
        else:
            resp = 's'
    return print(f'\nTem {len(years_base)} pessoa{resp} com mais de 50 anos e menos de 60kg\n')

def height():
    height_base_mediaIdade = []
    for i in data_base:
        if data_base[i]['altura'] < 1.60:
            height_base_mediaIdade.append(data_base[i]['idade'])
        if len(height_base_mediaIdade) == 0 or len(height_base_mediaIdade) == 1:
            resp = ''
            respMedia = ''
        else:
            resp = 's'
            respMedia = f'a media de idade entre elas e {sum(height_base_mediaIdade) / len(height_base_mediaIdade):.2f} anos'
    return print(f'\nTem {len(height_base_mediaIdade)} pessoa{resp} com menos de 1.60m {respMedia}\n')
def blue_eyes():
    blue_eyes_base = []
    for i in data_base:
        if data_base[i]['cor dos olhos'] == 'Azul':
            blue_eyes_base.append(data_base[i]['cor dos olhos'])
        if len(blue_eyes_base) == 0 or len(blue_eyes_base) == 1:
            resp = ''
        else:
            resp = 's'
    return print(f'\nTem {len(blue_eyes_base)} pessoa{resp} com olhos azuis\n')

def hair_colors_ruivo_Blue_eyes():
    hair_colors_ruivo_Blue_eyes_base = []
    for i in data_base:
        if data_base[i]['cor dos cabelos'] == 'Ruivo' and data_base[i]['cor dos olhos'] == 'Azul':
            hair_colors_ruivo_Blue_eyes_base.append(data_base[i]['cor dos cabelos'])
        if len(hair_colors_ruivo_Blue_eyes_base) == 0 or len(hair_colors_ruivo_Blue_eyes_base) == 1:
            resp = ''
        else:
            resp = 's'
    return print(f'\nTem {len(hair_colors_ruivo_Blue_eyes_base)} pessoa{resp} com cabelos ruivos e olhos azuis\n')