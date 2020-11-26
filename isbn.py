def get_ISBN_ID (isbn):
    total = 0
    multiplier = 10
    for c in isbn.lower():
        if c == 'x':
            total += multiplier*10
        elif c == '?':
            pass
        else:
            total += multiplier*int(c)
        multiplier -= 1
        if multiplier == 0: break
    return total

def get_ISBN_valid (isbn):
    if get_ISBN_ID (isbn) % 11 == 0:
        return True
    return False

def swap_digits (i, j, st):
    arr = []
    for c in st:
        arr.append (c)
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t
    return ''.join (arr)

# QUESTION 1
##inpt = input ("Enter a valid ISBN leaving one digit as a '?': ")
##placevalue_multiplier = 10-inpt.find ('?')
##current = get_ISBN_ID (inpt)
##
##missing_digit = 0
##while ((current + (missing_digit*placevalue_multiplier)) % 11) != 0:
##    missing_digit += 1
##
##print ("Missing digit is", missing_digit)

# QUESTION 2
##while True:
##    print ("Valid" if get_ISBN_valid (input("Enter an ISBN: ")) else "Invalid")

# QUESTION 3
isbn = "3201014525"
validpossibles = []
for i in range (0, len(isbn)-1):
    for j in range (i, len(isbn)):
        swapped = swap_digits (i, j, isbn)
        if get_ISBN_valid (swapped):
            print (swapped, "is possible")
            validpossibles.append (swapped)
