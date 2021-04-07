c = 0
e = 0
verificadorCASA = 0
verificadorESC= 0
num=int(input("Digite o número de dias analisados."))
for i in range (0,num):
    SD, SN=input("Diga se fará sol ou chuva, na ida e na volta do trabalhom respectivamente, separado por espaço.").split(' ')
    if len(SD)>len(SN): # Chuva e sol:
        if verificadorCASA==0:
            c+=1
            verificadorESC=1
        else:
            verificadorESC=1
    elif len(SD)==5 and len(SN)==5: #Chuva e chuva:
        if verificadorCASA==0:
            c+=1
            verificadorESC=1
        else:
            verificadorESC=1
        verificadorESC=1
    elif len(SD)<len(SN): #Sol e chuva:
        if verificadorESC==0:
            e+=1
            verificadorCASA=1
        else:
            verificadorCASA=1
print("{} {}".format(c,e))

