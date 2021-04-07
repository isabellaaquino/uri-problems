#def quantidade(num):
cont = 0
contPositivos = 0
soma = 0 
for c in range(0,6):
    num=float(input("Digite um número."))
    if num>=0:
        contPositivos+=1
        soma+=num
    cont+=1
media=soma/contPositivos
print(media)
# Fiquei em dúvida em como colocar uma função aqui :( Eu precisava invocar ela com alguma variável, que não soube qual.