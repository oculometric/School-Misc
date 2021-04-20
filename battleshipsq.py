ships_length = []
ships_rotate = [] # 0 -> left to right      1 -> bottom to top
ships_locate = [] # digits are formatted YX

shipsboard = [ # initialised to test config
[1,1,1,1,1,1,1,1,0,1],
[1,0,0,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0,0,0]
    ] # Should be indexed as [X][Y], 0 is an empty square, 1 is an occupied one

def r (sq, i=1):
    return ((sq//10)*10) + (((sq%10)+i)%10)
def l (sq, i=1):
    return ((sq//10)*10) + (((sq%10)-i)%10)
def u (sq, i=1):
    return ((((sq//10)+i)%10)*10) + (sq%10)
def d (sq, i=1):
    return ((((sq//10)-i)%10)*10) + (sq%10)

def set_square (sq, b):
    shipsboard[sq%10][sq//10] = b

def update_shipsboard ():
    global shipsboard
    shipsboard = []
    for i in range (10):
        arr = []
        for j in range (10):
            arr.append (0)
        shipsboard.append (arr)
    # TODO: Update board with ships
    for ship_ind in range (0, len(ships_length)):
        if ships_rotate[ship_ind] == 0:
            for i in range (0, ships_length[ship_ind]):
                set_square (r(ships_locate[ship_ind], i), 1)
        if ships_rotate[ship_ind] == 1:
            for i in range (0, ships_length[ship_ind]):
                set_square (u(ships_locate[ship_ind], i), 1)

def test_mini (sq):
    if shipsboard[sq%10][sq//10] == 1:
        return 1
    return 0
    
def test_square (sq): # Returns 0 if empty, 1 if occupied, 2 if adjacent to an occupied square
    if test_mini (sq) == 1: return 1
    if test_mini (r(sq)) == 1: return 2
    if test_mini (l(sq)) == 1: return 2
    if test_mini (u(sq)) == 1: return 2
    if test_mini (d(sq)) == 1: return 2
    if test_mini (u(r(sq))) == 1: return 2
    if test_mini (d(r(sq))) == 1: return 2
    if test_mini (u(l(sq))) == 1: return 2
    if test_mini (d(l(sq))) == 1: return 2
    return 0

def add_ship_if_valid (length, rotate, locate): # Returns 0 if success, 1 if ship would be in an invalid position
    test_squares = []
    if rotate == 0:
        for i in range (0, length):
            test_squares.append (r(locate, i))
    if rotate == 1:
        for i in range (0, length):
            test_squares.append (u(locate, i))
    for sq in test_squares:
        if sq > 100 or sq < 0:
            return 1
        if test_square != 0:
            return 1
    ships_length.append (length)
    ships_rotate.append (rotate)
    ships_locate.append (locate)

    update_shipsboard ()
    return 0

def print_shipsboard ():
    for y in range (0, 10):
        for x in range (0, 10):
            if shipsboard[x][9-y] == 1:
                print ("x", end='')
            else:
                print (" ", end='')
            print (" ", end='')
            if x == 9:
                print ("")
#print_shipsboard()
#update_shipsboard()
#print_shipsboard()
update_shipsboard()
add_ship_if_valid (5, 0, 00)
print_shipsboard()
