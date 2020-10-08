password = input ("Enter a password: ")
password = password.upper ()

def nextIndexOf (ch, st, dex):
    n = dex+1
    while n < len(st):
        if st[n] == ch:
            return n
        n = n+1
    return -1
    
rejected = False

for i in range (0, len(password)):
    nextInd = nextIndexOf (password[i], password, i)
    if nextInd < 0:
        continue
    lenSect = nextInd - i
    if nextInd + lenSect > len(password):
        continue

    if password[i:i+lenSect] == password[nextInd:nextInd+lenSect]:
        print ("Rejected!")
        rejected = True
        break

if not rejected:
    print ("Accepted!")
