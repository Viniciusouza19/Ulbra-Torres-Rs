#Import de tabulaçao
from tabulate import tabulate

#FUnçao input modificado
def input2(txt):
    print('*'*len(txt))
    input2(txt)
    print('*'*len(txt))
#Funçao de pesquisa em banco de dados simples
def pesq_funcionario(dicionario, nome):
    chaves = []
    for chave in dicionario:
        if chave.startswith(nome):
            chaves.append(chave)
    return chaves

#Funçao de imprimir tabulate
def imprime_funcionario(banco_funcionario, chaves):
    table = []
    for chave in chaves:
        table.append([
            banco_funcionario[chave]["numero-funcionario"],
            banco_funcionario[chave]["nome"],
            banco_funcionario[chave]["tempo-servico"],
            banco_funcionario[chave]["salario-bruto"],
            banco_funcionario[chave]["total-Desconto"],
            banco_funcionario[chave]["salario-liquido"]
            
        ])  
    print(tabulate(table, headers=["Numero do Funcionario","Nome","Tempo de serviço","Salario Bruto","Total de desconto","Salario Liquido"]))
    input('\nTecle enter para voltar ao menu inicial: ')