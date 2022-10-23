import json
with open('IdadeAlturaEpeso/personal_data.json', 'r') as file:
    data = json.load(file)

def mediaAltura_entre10_20():
    mediaAltura = []
    for i in data:
        if data[i]['years'] >=10 and data[i]['years'] <=20:
            mediaAltura.append(data[i]['height'])
    if len(mediaAltura) == 1:
        return f'Ha somente {len(mediaAltura)} pessoa com idade entre 10 e 20 anos e sua altura: {mediaAltura[0]}'
    elif len(mediaAltura) > 1:
        return f'A media de altura das pessoas entre 10 e 20 anos é: {sum(mediaAltura)/len(mediaAltura)}cm'
    else:
        return 'Nao ha pessoas entre 10 e 20 anos'

def amount_of_people():
    response = []
    for i in data:
        if data[i]['years'] > 50:
            response.append(data[i])
    if len(response) == 1:
        return  f'Ha {len(response)} pessoa com mais de 50 anos \n{response}'
    elif len(response) > 1:
        return f'Ha {len(response)} pessoas com mais de 50 anos \n{response}'
    else:
        'Nao ha pessoas com mais de 50 anos'
   

def calc_weight():
    response = []
    for i in data:
        if data[i]['weight'] < 40.0 and data[i]['weight'] > 0:
            response.append(data[i])
    if len(response) == 1:
        return f'Ha {len(response)} pessoa com peso inferior a 40kg \n{response}'
    elif len(response) > 1:
        return f'Ha {len(response)} pessoas com peso inferior a 40kg \n{response}'
    else:
        return 'Nao ha pessoas com peso inferior a 40kg'
