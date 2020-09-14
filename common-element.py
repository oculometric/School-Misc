import random
from datetime import datetime
import time

# declare
arr1 = []
arr2 = []
size = 100000

# populate
for i in range (1,size):
    arr1.append (random.randint (0, size*5))
    arr2.append (random.randint (0, size*5))

# search
def find (e, a):
    n = -1
    for i in a:
        n = n + 1
        if e is i:
            return n
    return -1
        

# time
start = datetime.now()

# traverse
common = False
c1 = -1
c2 = -1
for e1 in arr1:
    c1 = c1 + 1
    f = find (e1, arr2)
    if f != -1:
        common = True
        c2 = f
        break

# finalise
stop = datetime.now()
print((stop - start).total_seconds())

if common:
    print ("there was a common element")
    print (arr1[c1], arr2[c2])
