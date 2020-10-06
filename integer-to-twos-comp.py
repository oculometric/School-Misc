num = -1000
while num > 127 or num < -128:
    num = int(input ("Enter a number between -128 and 127: "))

    

bits = [0,0,0,0,0,0,0,0]
if num < 0:
    bits[0] = 1
    num += 128

if num >= 64:
    bits[1] = 1
    num -= 64
if num >= 32:
    bits[2] = 1
    num -= 32
if num >= 16:
    bits[3] = 1
    num -= 16
if num >= 8:
    bits[4] = 1
    num -= 8
if num >= 4:
    bits[5] = 1
    num -= 4
if num >= 2:
    bits[6] = 1
    num -= 2
if num >= 1:
    bits[7] = 1
    num -= 1

print (bits)
