
plaintext = input ("Enter some plaintext (spaces will not be preserved): ").lower()
while True:
    key = int(input ("Enter a key: ")) % 26
    if key == 0:
        print ("No change!")
        continue
    ciphertext = ""
    for c in plaintext:
        if c != ' ':
            tmp = ord(c)+key
            if (tmp > ord('z')):
                tmp -= 26
            ciphertext += chr(tmp)
    print (plaintext + " -> " + ciphertext)
