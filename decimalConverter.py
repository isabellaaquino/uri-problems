# Enter a binary number (composed by 1's and 0's only) and it'll return the decimal form of it.
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
