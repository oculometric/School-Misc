import random

arr = []
size = 10
for i in range (1,size):
    arr.append (random.randint (0, size/2))

narr = []
i = 0
while i < len (arr):
    if (i < len (arr)-1) and arr[i] == arr[i+1]:
        i = i + 1
    narr.append (arr[i])
    i = i + 1


print ("Original:", arr)
print ("Deduplicated:", narr)
print (len(arr)-len(narr), "items were eliminated.")
