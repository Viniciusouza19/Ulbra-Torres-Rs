def lowerswage(arg):
    wage = []
    for i in arg:
        wage.append(arg[i]['Salario'])
    
    wage.sort(reverse=True)
    wage.pop(0)
    lowerwage = []
    for i in arg:
        for s in wage:    
            if s == arg[i]['Salario']:
                lowerwage.append(arg[s]['idade'])
                lowerswage.append(arg[s]['Genero'])
    return lowerwage
    
