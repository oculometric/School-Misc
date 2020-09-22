mf = open ("mf.txt", "w")
mf.write ("A list of ")
mf.write ("squares\n")
for i in range(1000):
    mf.write (f'{i}\t{i**2}\n')
mf.close()
