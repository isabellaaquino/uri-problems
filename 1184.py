op=input("Digite a operação desejada com os elementos da matriz.\nDeve ser 'S' ou 'M'.").upper()
while op!='S' and op!='M':
    print("Erro! A entrada deve ser 'S' ou 'M'.")
    op=(input("Digite a operação desejada com os elementos da matriz.\nDeve ser 'S' ou 'M'.")).upper()
matriz = list()
for c in range(12):
    lista = []
    for i in range(12):
        numero=int(input("Digite os números da linha."))
        lista.append(numero)
    matriz.append(lista)
soma = 0
verificador = 0
for linha in range(12):
    verificador+=1
    if linha!=0:
        for h in range(verificador-1):
            soma+=matriz[linha][h]
media=soma/56
if op=='S':
    print(soma)
else:
    print("{:.1f}".format(media))