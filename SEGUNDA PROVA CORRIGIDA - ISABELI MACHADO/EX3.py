#ISABELI MACHADO - TERCEIRA QUESTÃO SEGUNDA PROVA - 2137 - 26/09

pedidos = {}

def adicionar(): 
    pedido = []
    nome = input("escreva nome do cliente? ")
    q = int(input("quantos pratos você vai querer? "))
    for i in range(q):
        pedidoa = input(f"escreva o pedido {i + 1}: ")
        pedido.append(pedidoa)
    pedidos.update({nome: pedido})

def atualizar():  
    cliente = input("nome do cliente para atualizar o pedido: ")
    if cliente in pedidos:
        pedidoant = input('escreva o pedido para atualizar: ')
        if pedidoant in pedidos[cliente]:
            i = pedidos[cliente].index(pedidoant)
            pedidoNovo = input("escreva o novo pedido: ")
            pedidos[cliente][i] = pedidoNovo
        else:
            print("o pedido original não está disponivel")
    else:
        print("O cliente não está disponivel")

def remover():  
    cliente = input("escreva o nome do cliente para remover o pedido: ")
    if cliente in pedidos:
        pedidoant = input('escreva o pedido para remover: ')
        if pedidoant in pedidos[cliente]:
            pedidos[cliente].remove(pedidoant)
        else:
            print("o pedido original não está disponivel")
    else:
        print("o cliente não está disponivel")

def filtrar(): 
    cliente = input("escreva o nome do cliente para exibir os pedidos: ")
    if cliente in pedidos:
        print(f"os pedidos de {cliente} são: {pedidos[cliente]}")
    else:
        print("o cliente não esta disponivel")               

def visualizar(): 
    if pedidos:
        for cliente, pedido in pedidos.items():
            print(f"{cliente}: {pedido}")
    else:
        print("nenhum pedido disponivel")

while True:
    print("------ RESTAURANTE ------")
    
    op = input('\nP- Adicionar pedido\nA- Atualizar pedido\nR- Remover pedido\nF- Filtrar pedido\nV- Visualizar todos os pedidos\nS- Sair\nEscolha uma opção: ').lower()

    if op == 'p':
        adicionar()
    elif op == 'a':
        atualizar()
    elif op == 'r':
        remover()
    elif op == 'f':
        filtrar()
    elif op == 'v':
        visualizar()
    elif op == 's':
        print("obrigada por usar meu programa, adeus :)")
        break
    else:
        print("opção invalida, tente novamente!!!")
