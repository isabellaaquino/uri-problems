def stats(a,b,c,d,e,f):
    statSaques=(a/b)*100
    statBloqueios=(c/d)*100
    statAtaques=(e/f)*100
    print("PONTOS DE SAQUE: {:.2f} %. \nPONTOS DE BLOQUEIO: {:.2f} %. \nPONTOS DE ATAQUE: {:.2f} %.".format(statSaques,statBloqueios,statAtaques))


# Somadores:
somasq = 0
somabq = 0
somatk = 0
somasq1 = 0
somabq1 = 0
somatk1 = 0

numJogadores=int(input("Digite o número de jogadores."))
while numJogadores<1 or numJogadores>100:
    numJogadores=int(input("Digite o número de jogadores."))

for c in range(0,numJogadores):
    nome=input("Digite o nome do jogador.")
    saque, bloqueio, ataque=input("Digite o número de saques, bloqueios e ataques desse jogador. Separe com espaços.").split(' ')
    saque=int(saque)
    bloqueio=int(bloqueio)
    ataque=int(ataque)
    somasq+=saque
    somabq+=bloqueio
    somatk+=ataque
    saq1, bloq1, atk1=input("Digite o número de saques, bloqueios e ataques que tiveram SUCESSO desse jogador. Separa com espaços.").split(' ')
    saq1=int(saq1)
    bloq1=int(bloq1)
    atk1=int(atk1)
    somasq1+=saq1
    somabq1+=bloq1
    somatk1+=atk1

stats(somasq1,somasq,somabq1,somabq,somatk1,somatk)