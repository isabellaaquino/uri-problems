def maisRapido (a,b,c):
    if a==b or a==c or b==c:
        print("Empate")
    elif a>b and a>c:
        if b>c:
            print("Ian")
        else:
            print("Bruno")
    elif b>a and b>c:
        if c>a:
            print("Otavio")
        else:
            print("Ian")
    elif c>a and c>b:
        if a>b:
            print("Bruno")
        else:
            print("Otavio")


teste1,teste2,teste3=input("Digite os tempos em segundos do Otavio, Bruno e Ian, separados respectivamente por um espaço.").split(' ')
teste1=float(teste1)
teste2=float(teste2)
teste3=float(teste3)
maisRapido(teste1,teste2,teste3)