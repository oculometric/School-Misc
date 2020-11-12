i1 = input ("Enter a word: ")
i2 = input ("Enter a word: ")

def asciiSum (st):
    i = 0
    for ch in st:
        i += ord (ch)

    return i


s1 = asciiSum (i1)
s2 = asciiSum (i2)

if s1 > s2:
    print ("Word 1 has a greater sum")
elif s2 > s1:
    print ("Word 2 has a greater sum")
else:
    print ("The words have equal sums")
