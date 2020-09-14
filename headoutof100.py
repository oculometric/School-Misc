import random

print (f'{h} heads, {(h+2)} tails.'.format(h=len([a for a in range (1, 100) if random.randint (0, 1) == 1])))
