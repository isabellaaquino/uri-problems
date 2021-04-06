def findBinary(number, numberStr):
    number = int(number)
    for c in range(32):
        if number//2 == 2:
            numberStr.insert(0,str(number%2))
            numberStr.insert(0,'10')
            break
        elif number//2 == 1:
            numberStr.insert(0,str(number%2))
            numberStr.insert(0,'01')
            break
        numberStr.insert(0,str(number%2))
        number = int(number/2)
    
    if len(numberStr)<32:
        for c in range(31 - len(numberStr)):
            numberStr.insert(0,'0')


def findDecimal(n):
    n = str(n)
    n = reversed(n)
    final = 0
    for i, c in list(enumerate(n)):
        if c == '1':
            final+= 2**i
    
    return final


number1, number2 = input("teste").split()
number1Str = []
number2Str = []
findBinary(number1, number1Str)
findBinary(number2, number2Str)
number1Str = ''.join(number1Str)
number2Str = ''.join(number2Str)
result = []
for c in range(32):
    if number1Str[c] == number2Str[c]:
        result.append('0')
    elif number1Str[c] == '1' and number2Str[c] == '0':
        result.append('1')
    elif number1Str[c] == '0' and number2Str[c] == '1':
        result.append('1')
result = ''.join(result)
print(findDecimal(result))