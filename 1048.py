def aumento(a):
    if 0<=a<=400:
        reajuste=a*115/100
        ganho=reajuste - a
        print("Novo salário: R$ {:.2f}\nReajuste ganho: R$ {:.2f}\nEm percentual: 15 %".format(reajuste,ganho))
    elif 400<a<=800:
        reajuste2=a*112/100
        ganho2=reajuste2 - ganho2
        print("Novo salário: R$ {:.2f}\nReajuste ganho: R$ {:.2f}\nEm percentual: 12 %".format(reajuste2,ganho2))
    elif 800<a<=1200:
        reajuste3=a*11/10
        ganho3=reajuste3 - a
        print("Novo salário: R$ {:.2f}\nReajuste ganho: R$ {:.2f}\nEm percentual: 10 %".format(reajuste3,ganho3))
    elif 1200<a<=2000:
        reajuste4=a*107/100
        ganho4=reajuste4 - a
        print("Novo salário: R$ {:.2f}\nReajuste ganho: R$ {:.2f}\nEm percentual: 7 %".format(reajuste4,ganho4))
    else:
        reajuste5=a*104/100
        ganho5=reajuste5 - a
        print("Novo salário: R$ {:.2f}\nReajuste ganho: R$ {:.2f}\nEm percentual: 4 %".format(reajuste5,ganho5))


salario=float(input("Digite seu salário."))
aumento(salario)
        