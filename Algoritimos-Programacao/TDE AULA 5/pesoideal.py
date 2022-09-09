sexo = input("Digite seu sexo [M/F]: ").lower()
altura = float(input("Digite sua altura: ").replace(',','.'))
if sexo == 'm':
    print(f'Seu peso ideal é {(72.7*altura)-58:.2f}Kg')

else:
    print(f'Seu peso ideal é {(62.1*altura)-44.7:.2f}Kg')