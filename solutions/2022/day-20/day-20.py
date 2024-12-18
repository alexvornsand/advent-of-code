# advent of code 2022
# day 20

# part 1
encryptedCode = [int(x) for x in open('input.txt', 'r').read()[:-1].split('\n')]

def decryptCode(encryptedCode, partTwo=False):
    if partTwo is False:
        code = [(i, encryptedCode[i]) for i in range(len(encryptedCode))]
        n = 1
    else:
        code = [(i, (encryptedCode[i] * 811589153) ) for i in range(len(encryptedCode))]
        n = 10
    for c in range(n):
        for i in range(len(code)):
            digit = [d for d in code if d[0] == i][0]
            origin = code.index(digit)
            code.pop(origin)
            destination = (origin + digit[1]) % len(code)
            code.insert(destination, digit)
    code = [d[1] for d in code]
    return(code[(code.index(0) + 1000) % len(code)] + code[(code.index(0) + 2000) % len(code)] + code[(code.index(0) + 3000) % len(code)])

decryptCode(encryptedCode)

# part 2
decryptCode(encryptedCode, True)