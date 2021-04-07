num=int(input("Digite o número de testes."))
for i in range(0,num):
    teste=input("Digite a sequência de 3 caracteres. Deve seguir o padrão: 1 dígito + 1 caractere + 1 dígito.")
    a=int(teste[0])
    c=int(teste[2])
    final=teste.upper()
    if a==c:
        print(a*c)
    elif teste==final:
        print(c-a)
    else:
        print(a+c)