def fotos(x,y,l1,h1,l2,h2):
    if (l1+l2<=x and h1+h2<=y) or (l1+l2+<=y and h1+h2<=x):
        print("S")
    elif (l1+h1<=x and l2+h2<=y) or (l1+h1<=y and l2+h2<=x):
        print("S")
    elif (l1+h2<=x and l2+h1<=y) or (l1+h2<=y and l2+h1<=x):
        print("S")
    if max(l1,l2)
    else:
        print("N")
    

largura,altura=input("Digite a largura e altura do álbum, em centímetros, separadas respectivamente por um espaço.").split(' ')
largura=int(largura)
altura=int(altura)
larg1,alt1=input("Digite a largura e a altura da primeira foto.").split(' ')
larg1=int(larg1)
alt1=int(alt1)
larg2,alt2=input("Digite a largura e a altura da segunda foto.").split(' ')
larg2=int(larg2)
alt2=int(alt2)

fotos(largura,altura,larg1,alt1,larg2,alt2)