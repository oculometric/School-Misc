# 0 = BLUE
# 1 = RED
import random

prisoners = []
total = 100
alive = total
blue = 0
for i in range (0, total):
    if random.randint (0, 1):
        prisoners.append (1)
    else:
        prisoners.append (0)
        blue += 1

print (prisoners)
print ("there are", blue, "blues")

def numbluevisible (i):
    a = 0
    for x in range (i+1, total):
        if prisoners[x] == 0:
            a += 1
    return a

def escape (i, c):
    global alive
    if prisoners[i] != c:
        alive -= 1
    #    print (i, "shouted", c, "and died")
    #else: print (i, "shouted", c, "survived")

evenblues = True
lastshout = 0
for i in range (0, total):
    if i == 0:
        if numbluevisible(i) % 2 == 0:
            lastshout = 0
            evenblues = True
            escape (i, 0) # Tell the others there are an even number of blues
        else:
            evenblues = False
            lastshout = 1
            escape (i, 1) # Tell the others there are an odd number of blues
    elif i == 1:
        bv = numbluevisible (i)
        if evenblues == True:
            if bv % 2 == 0:
                lastshout = 1
                escape (i, 1) # I must be red (last was even, so was this)
            if bv % 2 == 1:
                lastshout = 0
                escape (i, 0) # I must be blue (last was even, but not this)
        else:
            if bv % 2 == 0:
                lastshout = 0
                escape (i, 0) # I must be blue (last was odd, but not this)
            if bv % 2 == 1:
                lastshout = 1
                escape (i, 1) # I must be blue (last was odd, so was this)
    else:
        bv = numbluevisible (i)
        if (evenblues and lastshout == 0) or ((not evenblues) and lastshout == 1):
            evenblues = False
        else:
            evenblues = True
        
        if evenblues == True:
            if bv % 2 == 0:
                lastshout = 1
                escape (i, 1) # I must be red (last was even, so was this)
            if bv % 2 == 1:
                lastshout = 0
                escape (i, 0) # I must be blue (last was even, but not this)
        else:
            if bv % 2 == 0:
                lastshout = 0
                escape (i, 0) # I must be blue (last was odd, but not this)
            if bv % 2 == 1:
                lastshout = 1
                escape (i, 1) # I must be blue (last was odd, so was this)
            


print (alive, "survived.")
    
        
    
