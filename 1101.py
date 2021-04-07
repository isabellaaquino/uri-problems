num1=int(input("Digite o primeiro valor inteiro."))
num2=int(input("Digite o segundo valor inteiro."))
while num1==0 or num2==0:
    print("Nenhum dos números pode ser 0. Escolha outros valores.")
    num1=int(input("Digite o primeiro valor inteiro."))
    num2=int(input("Digite o segundo valor inteiro."))
if num1==num2:
    print("SOMA = 0")
if num1>num2:
    soma1 = 0
    for c in range(num2,num1+1):
        soma1+=c
        print(c, end=" ")
    print("SOMA = {}".format(soma1))
elif num2>num1:
    soma2 = 0
    for i in range(num1,num2+1):
        soma2+=i
        print(i, end=" ")
    print("SOMA = {}".format(soma2))


