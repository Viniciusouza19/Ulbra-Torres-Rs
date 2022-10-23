def profit(acoes_date):
    for acao, price in acoes_date.items():
        profit = price['priceSeller'] - price['priceBuy']
        if profit > 0:
            print(f"\nA ação {acao} teve um lucro de R${profit:.2f}")
        else:
            print(f"\nA ação {acao} teve um prejuízo de R${profit:.2f}")

def profit_top(acoes_date):
    for acao, price in acoes_date.items():
        if price['priceSeller'] - price['priceBuy'] > 1000:
            print(f"\nA ação {acao} teve um lucro de R${price['priceSeller'] - price['priceBuy']:.2f} superando R$1000,00")

def profit_lower(acoes_date):
    for acao, price in acoes_date.items():
        if price['priceSeller'] - price['priceBuy'] < 200:
            print(f"\nA ação {acao} teve um lucro inferior a 200 de R${price['priceSeller'] - price['priceBuy']:.2f}")

def profit_total(acoes_date):
    total = 0
    for acao, price in acoes_date.items():
        total += price['priceSeller'] - price['priceBuy']
        if total > 0:
            print(f"\nO total de lucro foi de R${total:.2f}")
        else:
            print(f"\nO total de prejuízo foi de R${total:.2f}")