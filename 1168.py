num=int(input("Digite o número de testes."))
for c in range(0,num):
    soma = 0
    leds=input("Digite o número que João quer montar com LEDS.")
    conta0=leds.count('0') * 6
    soma+=conta0
    conta1=leds.count('1') * 2
    soma+=conta1
    conta2=leds.count('2') * 5
    soma+=conta2
    conta3=leds.count('3') * 5
    soma+=conta3
    conta4=leds.count('4') * 4
    soma+=conta4
    conta5=leds.count('5') * 5
    soma+=conta5
    conta6=leds.count('6') * 6
    soma+=conta6
    conta7=leds.count('7') * 3
    soma+=conta7
    conta8=leds.count('8') * 7
    soma+=conta8
    conta9=leds.count('9') * 6
    soma+=conta9
    print("{} leds".format(soma))