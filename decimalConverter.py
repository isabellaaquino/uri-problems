def findDecimal(n):
    n = str(n)
    n = reversed(n)
    final = 0
    for i, c in list(enumerate(n)):
        if c == '1':
            final+= 2**i
    
    return final


number = int(input("Type a binary number."))
print(findDecimal(number))