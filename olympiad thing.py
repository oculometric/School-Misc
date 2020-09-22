def generatetable (inp, limit=-1):
    rows = []
    rows.append ([])

    rows[0] = inp

    rowsize = len (rows[0])
    row = 0
    while (limit<0 and rowsize > 1) or (limit>-1 and row < limit):
        rows.append ([])
        for i in range (0, rowsize-1):
            a = rows[-2][i]
            b = rows[-2][i+1]
            if a == b:
                rows[-1].append(a)
            else:
                l = ['R', 'G', 'B']
                l.remove (a)
                l.remove (b)
                rows[-1].append(l[0])
        rowsize = len(rows[-1])
        row += 1

    return rows[-1]

# QUESTION 1A
print ("Welcome. Please type in uppercase letters R, G, or B for the algorithm")

isGood = False
inp = ''
while not isGood:
    inp = input ("Type the sequence: ").upper()
    if len (inp) > 0:
        isGood = True
    for c in inp:
        if c != 'R' and c != 'G' and c != 'B':
            print ("Invalid input")
            isGood = False
            break
print (generatetable(list(inp)))

# QUESTION 1B
results = []
inp = list("RRRRRRRRR")
while inp != list("BBBBBBBBB"):
    out = generatetable (inp, limit=1)
    if out == list("RRGBRGBB"):
        results.append (inp[:])

    n = 0
    while True:
        if inp[n] == "R":
            inp[n] = "G"
            break
        elif inp[n] == "G":
            inp[n] = "B"
            break
        elif inp[n] == "B":
            inp[n] = "R"
            n+=1
print (results)
print (len(results))

# QUESTION 1C
# R _ (must be B given the rules)
#  G
# Given that two of the squares in a triangle are known, the other can be logically assumed to be only one value, based on the rules.
# Given that the start of each row is know, this technique can be applied over the whole structure of the triangle, giving only one valid triangle for the given set of first row items

# QUESTION 1D
lengthsWithProperty = []
for i in range (6, 30):
    lengthsWithProperty.append (i)
    inp = ['R' for c in range (0, i)]
    print (f"Trying length {i}")
    while not (inp[-1] == 'B' and inp[0] == 'B'):
        out = generatetable (inp)
        if out != generatetable ([inp[0], inp[-1]]):
            lengthsWithProperty.pop()
            break

        n = 0
        while True:
            if inp[n] == "R":
                inp[n] = "G"
                break
            elif inp[n] == "G":
                inp[n] = "B"
                break
            elif inp[n] == "B":
                inp[n] = "R"
                n+=1

print (lengthsWithProperty)


