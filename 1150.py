def ultrapassar(a,b):
    cont = 1
    somador = 0
    for c in range(a,b):
        if somador>=b:
            break
        if c==a:
            somador=a
        if c!=a+1:
            somador+=c
            cont+=1

    print(cont)
    

X=int(input("Digite o valor de X."))
Y=int(input("Digite o valor de Y."))
while Y<=X:
    Y=int(input("Digite o valor de Y."))
ultrapassar(X,Y)
        