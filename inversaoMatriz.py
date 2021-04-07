matriz = input("Digite uma lista composta (matriz")
matrizFinal = []
matrizFinal = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
print(matrizFinal)
