integerinput = int(input ("Enter a number: "))

stringoutput = ""
NUMERALS = ['I', 'V', 'X', 'L', 'C', 'D', 'M', '◊']

def getNumerals (n):
    if n > 9:
        return getNumerals (int(n/10))
    out = ""
    if n < 4:
        for x in range (0, n):
            out += 'I'
    elif n < 5:
        out = 'IV'
    elif n < 9:
        out = 'V'
        for x in range (0, n-5):
            out += 'I'
    else:
        out = 'IX'

    return out

def incrementNumerals (st, n):
    if (n == 0): return st
    out = ""
    for l in st:
        out += NUMERALS[NUMERALS.index (l)+(2*n)]
    return out

output = ""
p = len(str(integerinput))-1
for s in str(integerinput):
    output = output + incrementNumerals (getNumerals (int(s)), p)
    p -= 1

print (output)
