num=int(input("Digite o número de comandos que serão dados pelo sargento. Caso seja 0, o programa parará."))
while num>0:
    if num==0:
        break
    direcao=input("Digite os comandos do sargento. (Devem ser 'D' ou/e 'E'.").upper()
    posD=direcao.count('D') * 0.25
    posE=direcao.count('E') * -0.25
    soma = posE + posD
    final = abs(soma - int(soma))
    if direcao.count('D')==direcao.count('E') or final==0:
        print('N')
    elif final==0.25:
        print('L')
    elif final==0.5:
        print('S')
    elif final==0.75:
        print('N')
    num=int(input("Digite o número de comandos que serão dados pelo sargento."))