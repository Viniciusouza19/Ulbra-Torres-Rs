import funcoes
import os
acoes_date = {}
cont = 0
while True:
    os.system('clear') or None
    cont += + 1
    acao = input(f"{cont}-Digite a sigla ação na bolsa de valores: ").upper()
    if acao == 'F':
        break
    purchase_price = float(input(f"\nDigite o preço de COMPRA da ação {acao}: "))
    sale_price = float(input(f"\nDigite o preço de VENDA da ação {acao}: "))
    acoes_date[acao] = {'priceBuy':purchase_price,'priceSeller':sale_price}
    
funcoes.profit(acoes_date)
funcoes.profit_top(acoes_date)
funcoes.profit_lower(acoes_date)
funcoes.profit_total(acoes_date)