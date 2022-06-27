def digits (n):
    if (n < 10): return [n]
    return [(n % 10)] + digits(n//10)

def do_harshad (n):
    i = 1
    last = -1
    r = 1
    while (i <= n):
        if (r % sum(digits(r)) == 0):
            print ("Found "+str(r))
            last = r
            i += 1
        r += 1
    return last

while True:
    n = int(input("Enter a number: "))
    last = do_harshad (n)
    print ("The " + str(n) + "th Harshad number is " + str(last))

