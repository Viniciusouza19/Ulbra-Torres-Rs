cont = 0
sums = []
while True:
    cont = cont + 1
    age = int(input(f'{cont}-Digite uma idade ou zero para sair: '))
    sums.append(age)
    if age == 0:
        cont = cont - 1
        break
    

print(f'A média de idades das {cont} pessoas : {sum(sums)//cont} anos')