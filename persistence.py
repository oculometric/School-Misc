value = int(input ("Enter integer (0-99): "))
operation = input ("Calculate additive or multiplicative persistence (a or m)? ").lower()

count = 0
while value > 9:
    value = (value//10) + (value%10) if (operation == "a") else (value//10) * (value%10)
    count += 1
print ("The persistence is:", count) 
