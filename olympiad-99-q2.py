import random
import time

GRID_SIZE = 10
NUM_ATOMS = 5

# blackbox = [[x ->]
#             [y   ]
#             [|   ]
#             [\/  ]]
# reference as blackbox[y][x]

blackbox = [[0 for x in range (0, GRID_SIZE)] for x in range (0, GRID_SIZE)]

def generateBoxGrid ():
    global blackbox
    blackbox = [[0 for x in range (0, GRID_SIZE)] for x in range (0, GRID_SIZE)]
    for i in range (0, NUM_ATOMS):
        r1 = random.randint (1, GRID_SIZE-2)
        r2 = random.randint (1, GRID_SIZE-2)
        while blackbox[r1][r2] == 1:
            r1 = random.randint (1, GRID_SIZE-2)
            r2 = random.randint (1, GRID_SIZE-2)
        blackbox[r1][r2] = 1

def printBoxGrid ():
    global blackbox
    print (" "+"".join(['-' for x in range (0, GRID_SIZE)]))
    for i in range (0, GRID_SIZE):
        line = ""
        for j in range (0, GRID_SIZE):
            if blackbox[i][j] == 1:
                line = line + "A"
            elif blackbox[i][j] == 2:
                line = line + "+"
            elif blackbox[i][j] == 3:
                line = line + "*"
            else:
                line = line + "."
        print ("|"+line+"|")
    print (" "+"".join(['-' for x in range (0, GRID_SIZE)]))

def getParticle (x, y):
    if (x < 0): return False
    if (y < 0): return False
    if (x >= GRID_SIZE): return False
    if (y >= GRID_SIZE): return False
    return (blackbox[y][x] == 1)

def coordsToPlace (x, y):
    side = "_"
    offset = 0
    if x < 0:
        side = "L"
        offset = GRID_SIZE-y
    elif x >= GRID_SIZE:
        side = "R"
        offset = GRID_SIZE-y
    elif y < 0:
        side = "T"
        offset = x+1
    elif y >= GRID_SIZE:
        side = "B"
        offset = x+1

    return side + " " + str (offset)

def rayCast (coord, direction):
    result = "null"
    newCoord = coord
    newDirection = direction
    while (True):
        if newDirection == 0: # +x
            newCoord[0] += 1
            if not getParticle(newCoord[0]+1, newCoord[1]):
                if getParticle(newCoord[0]+1, newCoord[1]-1):
                    newDirection = 1
                if getParticle(newCoord[0]+1, newCoord[1]+1):
                    newDirection = 3
                    if getParticle(newCoord[0]+1, newCoord[1]-1):
                        newDirection = 2
                        result = "Reflected"
        elif newDirection == 1: # +y
            newCoord[1] += 1
            if not getParticle(newCoord[0], newCoord[1]+1):
                if getParticle(newCoord[0]-1, newCoord[1]+1):
                    newDirection = 0
                if getParticle(newCoord[0]+1, newCoord[1]+1):
                    newDirection = 2
                    if getParticle(newCoord[0]-1, newCoord[1]+1):
                        newDirection = 3
                        result = "Reflected"
        elif newDirection == 2: # -x
            newCoord[0] -= 1
            if not getParticle(newCoord[0]-1, newCoord[1]):
                if getParticle(newCoord[0]-1, newCoord[1]-1):
                    newDirection = 1
                if getParticle(newCoord[0]-1, newCoord[1]+1):
                    newDirection = 3
                    if getParticle(newCoord[0]-1, newCoord[1]-1):
                        newDirection = 0
                        result = "Reflected"
        else: # -y
            newCoord[1] -= 1
            if not getParticle(newCoord[0], newCoord[1]-1):
                if getParticle(newCoord[0]-1, newCoord[1]-1):
                    newDirection = 0
                if getParticle(newCoord[0]+1, newCoord[1]-1):
                    newDirection = 2
                    if getParticle(newCoord[0]-1, newCoord[1]-1):
                        newDirection = 1
                        result = "Reflected"
        if (newCoord[0] < 0 or newCoord[0] >= GRID_SIZE or newCoord[1] < 0 or newCoord[1] >= GRID_SIZE):
            break
        elif getParticle(newCoord[0], newCoord[1]):
            blackbox[newCoord[1]][newCoord[0]] = 3
            result = "Absorbed"
            break
        else:
            blackbox[newCoord[1]][newCoord[0]] = 2
    if result == "null":
        return "Exited at " + coordsToPlace (newCoord[0], newCoord[1])
    return result

def runSim (side, offset):
    if side == 'T':
        print (rayCast ([offset-1, -1], 1))
    if side == 'B':
        print (rayCast ([offset-1, GRID_SIZE], 3))
    if side == 'L':
        print (rayCast ([-1, GRID_SIZE-(offset)], 0))
    if side == 'R':
        print (rayCast ([GRID_SIZE, GRID_SIZE-(offset)], 2))

def cleanBox ():
    for i in range (0, GRID_SIZE):
        for j in range (0, GRID_SIZE):
            if blackbox[i][j] == 2:
                blackbox[i][j] = 0
            if blackbox[i][j] == 3:
                blackbox[i][j] = 1

## MAIN STARTS HERE ##

print ("Welcome to the black box simulator!")
print (f"Type a pair of integers separated by a space. They must both be between 1 and {GRID_SIZE} inclusive.")
i = 0
while i < 5:
    inn = input ("Int pair: ")
    s = inn.split (' ')
    try:
        if len (s) < 2: continue
        x = int (s[0])
        if x > GRID_SIZE or x < 1: continue
        y = int (s[1])
        if y > GRID_SIZE or y < 1: continue
        blackbox[GRID_SIZE-(y)][x-1] = 1
        print ("Successfully read coord!")
        i += 1
    except:
        i = i


#generateBoxGrid ()
print ("Here is your grid: ")
printBoxGrid()
while (True):
    inp = input (f"Enter T,B,L,R followed by a number between 1 and {GRID_SIZE}, or X 0 to exit: ")
    s = inp.split (' ')
    if len (s) < 2: continue
    o = int(s[1])
    if o < 1 or o > GRID_SIZE: continue
    if s[0] == 'X' and o == 0:
        break
    elif s[0] == 'T' or s[0] == 'B' or s[0] == 'L' or s[0] == 'R':
        runSim (s[0], o)
        printBoxGrid()
        time.sleep (1)
        cleanBox ()
        printBoxGrid()
