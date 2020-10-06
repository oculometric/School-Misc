import random

stockValue = 100
roundedStockValue = 100

def truncate (i, n):
    tmp = i * (10**n)
    tmp = int (tmp)
    tmp /= (10**n)
    return tmp

for i in range (1, 1000000):
    fluc = (random.random ()/10)-0.05
    stockValue += fluc
    roundedStockValue = truncate (roundedStockValue + fluc, 3)

print ("Real value", stockValue, "Truncated value", roundedStockValue)
