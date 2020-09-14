arr = []
inputVal = input ("Type a name: ")
while len(inputVal) > 0:
    arr.append (inputVal)
    inputVal = input ("Type another name, or press enter to continue: ")

arr.sort()
for s in arr:
    print (s, ", length is", len(s))

