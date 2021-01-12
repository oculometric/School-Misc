def fix (st):
    s = ""
    for c in st:
        if ord (c) >= ord('a') and ord (c) <= ord ('z'):
            s += c
    return s

plaintext = fix(input ("Enter some plaintext (spaces will not be preserved): ").lower())
while True:
    key = list(fix(input ("Enter a key: ").lower()))
    print (key)
    ciphertext = ""
    i = 0
    for c in plaintext:
        if c != ' ':
            tmp = ord(c)+(ord(key[i])-ord('a'))
            if (tmp > ord('z')):
                tmp -= 26
            ciphertext += chr(tmp)
            i += 1
            if i >= len(key):
                i = 0
    print (plaintext + " -> " + ciphertext)
