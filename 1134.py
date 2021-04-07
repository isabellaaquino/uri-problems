entrada=int(input("Escolha o tipo de combustível consultado.\n 1.Álcool 2.Gasolina 3.Diesel 4.Fim do programa."))
while 4>=entrada>=1:
    print("MUITO OBRIGADO.")
    if entrada==1:
        print("Álcool: 1")
        entrada=int(input("Escolha o tipo de combustível consultado.\n 1.Álcool 2.Gasolina 3.Diesel 4.Fim do programa."))    
    elif entrada==2:
        print("Gasolina: 2")
        entrada=int(input("Escolha o tipo de combustível consultado.\n 1.Álcool 2.Gasolina 3.Diesel 4.Fim do programa."))
    elif entrada==3:
        print("Diesel: 0")
        entrada=int(input("Escolha o tipo de combustível consultado.\n 1.Álcool 2.Gasolina 3.Diesel 4.Fim do programa."))
    elif entrada==4:
        break
while entrada!=[1,2,3,4]:
    entrada=int(input("Escolha o tipo de combustível consultado.\n 1.Álcool 2.Gasolina 3.Diesel 4.Fim do programa."))
