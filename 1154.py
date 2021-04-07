def media(a):
    soma = a
    cont = 1
    while a>=0:
        a=int(input("Digite um inteiro."))
        if a<0:
            break
        soma = soma + a
        cont+=1
    media=soma/cont
    print("{:.2f}".format(media))


inteiro=int(input("Digite um inteiro."))
media(inteiro)
