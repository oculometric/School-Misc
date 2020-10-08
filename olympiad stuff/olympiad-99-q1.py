def sumdigits (n):
    st = str (n)
    total = 0
    for x in st:
        total += int(x)
    return total

def river (n, iterations=16384):
    arr = [n]
    for i in range (0, iterations):
        arr.append (arr[-1])
        arr[-1] += sumdigits (arr[-2])
    return arr


# QUESTION 1A

print (river (1, iterations=10))

n = int (input ("Enter a number: "))
arr = [n]
r1 = [1]
r3 = [3]
r9 = [9]
while True:
    if arr[-1] == r1[-1]:
        print ("Meeting river 1")
        break
    if arr[-1] == r3[-1]:
        print ("Meeting river 3")
        break
    if arr[-1] == r9[-1]:
        print ("Meeting river 9")
        break
    while arr[-1] < r1[-1]:
        arr.append (arr[-1])
        arr[-1] += sumdigits (arr[-2])
        if arr[-1] == r1[-1]:
            print ("Meeting river 1")
            break
    while arr[-1] > r1[-1]:
        r1.append (r1[-1])
        r1[-1] += sumdigits (r1[-2])
        if arr[-1] == r1[-1]:
            print ("Meeting river 1")
            break
    while arr[-1] > r3[-1]:
        r3.append (r3[-1])
        r3[-1] += sumdigits (r3[-2])
        if arr[-1] == r3[-1]:
            print ("Meeting river 3")
            break
    while arr[-1] > r9[-1]:
        r9.append (r9[-1])
        r9[-1] += sumdigits (r9[-2])
        if arr[-1] == r9[-1]:
            print ("Meeting river 9")
            break

print (arr[-1])
    
# QUESTION 1B

commonitems = {}
itemindex = {}
for i in range (1, 1000):
    for n in river (i, iterations=500):
        if n in commonitems:
            commonitems[n] += 1
            itemindex[n].append (i)
        else:
            commonitems[n] = 1
            itemindex[n] = [i]

for key in commonitems.keys():
    if commonitems[key] == 100:
        print ("Found", key, "in exactly 100 digital rivers")
        print ("The rivers were:", itemindex[key])
        

