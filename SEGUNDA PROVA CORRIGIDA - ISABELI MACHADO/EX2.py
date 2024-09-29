#ISABELI MACHADO - SEGUNDA QUESTÃO SEGUNDA PROVA - 2137 - 26/09

salarios = [] 
nomes = []
dicionario = {}
while True:
    nome = input("digite o nome do funcionario:\n")
    salario = int(input("digite o seu respequitivo salario:\n"))
    nomes.append(nome)
    salarios.append(salario)   
    def funcionario():
        dicionario.update({'nome':nome})
        dicionario.update({'salario':salario})
    funcionario() 

    minimo = int(input("digite o salario minimo da empresa:\n"))
    acima = (list(filter(lambda x: x>minimo,salarios))) 
    print(f'{acima} salario que está acima do minimo')
    aumento = (list(map(lambda x: x*1.2,acima))) 
    print(f'{aumento} salario que esta acima do minimo com aumento de 20%')

    somas = sum(salarios)
    medias = somas/len(salarios) 

    max_salario = max(salarios)
    min_salario = min(salarios) 

    print(f'o salário maximo: {max_salario}')
    print(f'o salario minimo: {min_salario}')

    for key,value in dicionario.items():
        print(f'{key}:{value}')
    
    saida = input("voce quer sair do programa?se sim digite S:\n").lower() 
    if saida == "s":
        print('obrigada por usar meu programa, adeus :)')
        break

        
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    