import random

h = len([a for a in range (1, 100) if random.randint (0, 1) == 1])
print (f'{h} heads, {(100-h)} tails.')

print ("test {(a)-10}".format (a=5))
