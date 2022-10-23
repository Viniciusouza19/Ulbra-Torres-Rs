while True:
    carPrice = float(input('Digite o preço do carro ou zero para sair: '))
    tableinstallments = {6: 0.03, 12: 0.06, 18: 0.09, 24: 0.12, 30: 0.15, 36: 0.18, 42: 0.21, 48: 0.24, 54: 0.27, 60: 0.30}
    print('\nTabela de parcelas: \n')
    for key, value in tableinstallments.items():
        parc = print(f'{key}x de R${(carPrice * value ) + carPrice / key:.2f} com juros de {value * 100}% ficara R${(carPrice * value ) + carPrice:.2f} no total')
    incash = print(f'\nÀ vista no dinheiro ou cheque com 20% de desconto fica R${carPrice-(carPrice * 0.2):.2f}\n')
    if carPrice == 0:
        break