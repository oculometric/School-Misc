import math

def is_prime (n):
    check_max = math.sqrt(n)
    prime = True

    for i in range (2, math.ceil(check_max)+1):
        if i != 2 and i % 2 == 0:
            continue
        if n % i == 0:
            prime = False
            break
    return prime
            
nums = []
print ("welcome")
while True:
    inp = input("enter a number, or nothing to exit: ")
    if inp == "":
        break
    num = int(inp)
    nums.append (num)

for n in nums:
    print (n, "is ", end='')
    if n <= 1:
        print ("not greater than 1")
    elif is_prime (n):
        print ("prime")
    else:
        print ("not prime")
    
    
