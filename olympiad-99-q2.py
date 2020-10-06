import random

GRID_SIZE = 10
NUM_ATOMS = 5

# blackbox = [[x ->]
#             [y   ]
#             [|   ]
#             [\/  ]]
# reference as blackbox[y][x]

blackbox = [[False for x in range (0, GRID_SIZE)] for x in range (0, GRID_SIZE)]

def generateBoxGrid ():
    global blackbox
    blackbox = [[False for x in range (0, GRID_SIZE)] for x in range (0, GRID_SIZE)]
    for i in range (0, NUM_ATOMS):
        r1 = random.randint (0, GRID_SIZE-1)
        r2 = random.randint (0, GRID_SIZE-1)
        while blackbox[r1][r2]:
            r1 = random.randint (0, GRID_SIZE-1)
            r2 = random.randint (0, GRID_SIZE-1)
        blackbox[r1][r2] = True

def printBoxGrid ():
    global blackbox
    print (" "+"".join(['-' for x in range (0, GRID_SIZE)]))
    for i in range (0, GRID_SIZE):
        line = ""
        for j in range (0, GRID_SIZE):
            if blackbox[j][i]:
                line = line + "x"
            else:
                line = line + " "
        print ("|"+line+"|")
    print (" "+"".join(['-' for x in range (0, GRID_SIZE)]))

def getParticle (x, y):
    if (x < 0) return false
    if (y < 0) return false
    if (x >= GRID_SIZE) return false
    if (y >= GRID_SIZE) return false
    return blackbox[y][x]
    
def rayCast (coord, direction):
    newCoord = coord
    newDirection = direction
    while (True):
        if direction == 0: # +x
            newCoord[0] += 1
            if getParticle(newCoord[0]+1, newCoord[1]-1):
                direction = 1
            if getParticle(newCoord[0]+1, newCoord[1]+1):
                direction = 3
                if getParticle(newCoord[0]+1, newCoord[1]-1):
                    direction = 2
        elif direction == 1: # +y
            newCoord[1] += 1
            if getParticle(newCoord[0]-1, newCoord[1]+1):
                direction = 0
            if getParticle(newCoord[0]+1, newCoord[1]+1):
                direction = 2
                if getParticle(newCoord[0]-1, newCoord[1]+1):
                    direction = 3
        elif direction == 2: # -x
            newCoord[0] -= 1
            if getParticle(newCoord[0]-1, newCoord[1]-1):
                direction = 1
            if getParticle(newCoord[0]-1, newCoord[1]+1):
                direction = 3
                if getParticle(newCoord[0]-1, newCoord[1]-1):
                    direction = 0
        else: # -y
            newCoord[1] -= 1
            if getParticle(newCoord[0]-1, newCoord[1]-1):
                direction = 0
            if getParticle(newCoord[0]+1, newCoord[1]-1):
                direction = 2
                if getParticle(newCoord[0]-1, newCoord[1]-1):
                    direction = 1
        if (newCoord[0] < 0 or newCoord[0] >= GRID_SIZE or newCoord[1] < 0 or newCoord[1] >= GRID_SIZE):
            break
    return newCoord

generateBoxGrid ()
printBoxGrid()
