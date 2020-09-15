import time
from datetime import datetime

ts1 = []
ts2 = []
for y in range (1,6):
    t = datetime.now ()
    for x in range(10000):
        ''.join( ['a','b','c','d','e','f','g'] )

    ts1.append (datetime.now()-t)
    print ("Tried using list with time", ts1[-1])

print ("Best was", min(ts1))
#print ("Average was", sum(ts1)/len(ts1))

for y in range (1,6):
    t = datetime.now ()
    for x in range(10000):
        ''.join( ('a','b','c','d','e','f','g') )

    ts2.append (datetime.now()-t)
    print ("Tried using tuple with time", ts2[-1])

print ("Best was", min(ts2))
#print ("Average was", sum(ts2)/len(ts2))



