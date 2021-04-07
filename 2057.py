def fuso(a,b,c):
    if a==0:
        final=24+b+c
        if final>=24:
            final0=final-24
            print(final0)
        else:
            print(final)
    else:
        final1=a+b+c
        if final1>=24:
            final2=final1-24
            print(final2)
        else:
            print(final1)
saida,tempo,fusoHorario=input("Digite o horário de saída, tempo de viagem e fuso horário do destino, respectivamente separados por espaços.").split(" ")
saida=int(saida)
tempo=int(tempo)
fusoHorario=int(fusoHorario)
fuso(saida,tempo,fusoHorario)
