#ISABELI MACHADO - PRIMEIRA QUESTÃO SEGUNDA PROVA - 2137 - 26/09

receitas = [] 
despesas = []
mesl = []

for i in range(12):
    ganhou = float(input(f'digite o que ganhou no mês {i + 1}: '))
    perdeu = float(input(f'digite o que gastou no mês {i + 1}: '))

    receitas.append(ganhou)
    despesas.append(perdeu)

    liquido = (list(map(lambda x,y: x-y,receitas,despesas))) 
    mesl.append(liquido)

    print(f'salario liquido:{liquido}') 
    
l_total = [sum(liquido)] 
media_a = (list(map(lambda x: x/12,l_total))) 
print(f'media anual: {media_a}') 
negativos = (list(filter(lambda x: x<0,liquido))) 
print(f'salarios negativos: {negativos}') 




