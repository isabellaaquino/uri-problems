n, m=input("Digite o número de participantes e o número de problemas, respectivamente, separados por espaços.").split()
n=int(n)
m=int(m)
while n!=0 and m!=0:
    if n==0 and m==0:
        break
    matriz = []
    matriz2 = []
    for c in range(n):
        coluna=[int(x) for x in input("Digite os valores da linha, separados por espaço.").split()]
        matriz.append(coluna)
    #Criação de uma matriz "inversa":
    matriz2=[[matriz[a][b] for a in range(len(matriz))] for b in range(len(matriz[0]))]
    # Condições:
    somador0= 0
    somador1= 0
    verificadorProbR = 0
    ngmResolveuTodos = True
    todosResolveram = 0
    alguemResolveu = 0
    for i in matriz:
        if i == [1,1,1]:
            todosResolveram+=1
            ngmResolveuTodos=False
        if 1 in i:
            verificadorProbR+=1
    for h in matriz2:
        if 1 in h:
            alguemResolveu+=1
        
    # Características alcançadas:
    cont = 0
    if ngmResolveuTodos:  
        cont+=1

    if verificadorProbR==3:
        cont+=1

    if todosResolveram==0:
        cont+=1

    if alguemResolveu==3:
        cont+=1
    print(cont)
    n, m=input("Digite o número de participantes e o número de problemas, respectivamente, separados por espaços.").split()
    n=int(n)
    m=int(m)