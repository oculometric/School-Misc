import random

GRID_SIZE = 10
NUM_ATOMS = 5

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

def projectRay (side, offset):
    # TODO
    return

generateBoxGrid ()
printBoxGrid()
        
    
