def coordenadas(x,y):
    while x!=0 and y!=0:
        if x>0 and y>0:
            print("primeiro")
        elif x>0 and y<0:
            print("quarto")
        elif x<0 and y>0:
            print("segundo")
        elif x<0 and y<0:
            print("terceiro")
        x=int(input("Digite a coordenada X. Caso ela seja 0, o programa parará."))
        y=int(input("Digite a coordenada Y. Caso ela seja 0, o programa parará."))
        if x==0 or y==0:
            break


xis,ips=input("Digite as coodernadas X e Y respectivamente separadas por espaço.").split(' ')
xis=int(xis)
ips=int(ips)
coordenadas(xis,ips)
