# Enter a decimal number up to 2**31 and it'll return the binary form of it with 32 bits.

number=int(input("Type a number."))
numberStr = []

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
    for c in range(32 - len(numberStr)):
        numberStr.insert(0,'0')
numberStr = ''.join(numberStr)
print(numberStr[:9]+' '+numberStr[9:17]+' '+numberStr[17:25]+' '+numberStr[25:32])