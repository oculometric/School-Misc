##while True:
##    f = open ("readFile.txt", "r+")
##    code1 = str (f.read(100000000000))
##    f.write (code1 + code1)
##    print (code1)
##    f.close ()
import random

content = "die"

for i in range (1, 100):
    name = ""
    for j in range (1, 20):
        name = name + (str(random.randint(97, 122)))
    f = open (name, "w")
    f.write (content)
    f.close()
