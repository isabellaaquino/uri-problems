Q=int(input("Digite o número de pessoas contempladas na pesquisa."))
V=[int(x) for x in input("Digite, Q vezes, se a pessoa ficou satisfeita ou não, com 1's ou 0's.").split()]
while len(V)>Q:
    print("Você colocou mais testes que pessoas na pesquisa.")
    V=[int(x) for x in input("Digite, Q vezes, se a pessoa ficou satisfeita ou não, com 1's ou 0's.")]
soma = 0
for i in V:
    if i==0:
        soma+=1

if soma > Q/2:
    print("S")
else:
    print('N')