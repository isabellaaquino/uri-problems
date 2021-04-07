def op():
    num=int(input("Digite o número da linha que será realizada a operação."))
    ope=input("Escolha a operação que será realizada. Deve ser 'S' ou 'M'.").upper()
    while ope!='M' and ope!='S':
        print("Erro! Deve ser 'S' ou 'M'.")
        op=input("Escolha a operação que será realizada. Deve ser 'S' ou 'M'.").upper()
    soma=sum(matriz[num])
    media=soma/12
    if op=='S':
        print(soma)
    else:
        print(media)


matriz = list()
for c in range(12):
    lista = []
    for i in range(12):
        numero=int(input("Digite os números da linha."))
        lista.append(numero)
    matriz.append(lista)
op()