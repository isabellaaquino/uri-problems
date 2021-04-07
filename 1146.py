testes=int(input("Digite o valor desejado. Caso digite 0, o programa parará."))
while testes!=0:
    for c in range (1,testes+1):
        print(c,end=" ")
    testes=int(input("Digite o valor desejado. Caso digite 0, o programa parará."))
    if testes==0:
        break