testes=int(input("Digite o número de testes desejado."))
for c in range (0,testes):
    soma1=0
    soma2=0
    x=int(input("Digite o primeiro inteiro."))
    y=int(input("Digite o segundo inteiro."))
    if x==y:
        print("0")
    elif y>x:
        for i in range (x+1,y):
            if i%2!=0:
                soma1+=i
        print(soma1)
    elif x>y:
        for p in range (y+1,x):
            if p%2!=0:
                soma2 = soma2 + p
        print(soma2) 

    

