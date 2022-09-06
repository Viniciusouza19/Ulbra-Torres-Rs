import os
nome = input("Digite seu nome: ")
tel = input("Digite seu telefone: ")
endereco = input("Digite seu endereço: ")
cep = input("Digite o cep da sua cidade: ")
os.system('clear') or None
print(f"Nome: {nome}\nTel: {tel}\nEndereço: {endereco}\nCep: {cep}")