cont = 0
dados = {}
import funcoes
while True:
    cont += 1
    age = int(input(f'{cont}-Digite a idade: '))
    if age < 0:
        break
    gender = input(f'{cont}-Digite o sexo \nM-Masculino\nF-Feminino\nDigite a opcao: ').lower()
    wage = float(input(f'{cont}-Digite o salario: ').replace(',','.'))
    dados[cont] = {'idade':age,'Genero':gender,'Salario':wage}

wageMediun = 0
for i in dados:
    wageMediun += dados[i]['Salario']
calcAge = []
for i in dados:
    calcAge.append(dados[i]['idade'])
    print(calcAge)

for i in dados:
    calcGender = []
    if dados[i]['Genero'] == 'f' and dados[i]['Salario'] <= 200:
        calcGender.append(dados[i]['Genero'])

    
print(f'A media do salario dos grupos e de R${wageMediun/cont:.2f}')

print(f'A idade maxima e de {max(calcAge)}')
print(f'A idade minima e de {min(calcAge)}')

print(f'A quantidade de mulheres com salario ate R$200 e de {len(calcGender)}')

print(f'A pessoas com menores salarios sao {funcoes.lowerswage(dados)}')


    

                