somaTotal = 0
somaCoelhos = 0
somaRatos = 0
somaSapos = 0
num=int(input("Digite o número de testes."))
for i in range(num):
    quantia, tipo=input("Digite a quantidade e o tipo de cobaia utilizado.").split(' ')
    quantia=int(quantia)
    tipo=tipo.upper()
    if tipo=='C':
        somaCoelhos+=quantia
        somaTotal+=quantia
    elif tipo=='R':
        somaRatos+=quantia
        somaTotal+=quantia
    elif tipo=='S':
        somaSapos+=quantia
        somaTotal+=quantia
coelhos=(somaCoelhos/somaTotal)*100
ratos=(somaRatos/somaTotal)*100
sapos=(somaSapos/somaTotal)*100
print("Total: {} cobaias\nTotal de coelhos: {}\nTotal de ratos: {}\nTotal de sapos: {}\nPercentual de coelhos: {:.2f} %\nPercentual de ratos: {:.2f} %\nPercentual de sapos: {:.2f} %".format(somaTotal,somaCoelhos,somaRatos,somaSapos,coelhos,ratos,sapos))