n_digits = int(input("How many digits? "))
digits = []
# Get input
for i in range(n_digits):
    digit = -1
    while (digit < 0 or digit > 9):
        try:
            digit = int(input("Enter a digit: "))
        except:
            print ("That wasn't a digit!")
    digits.append(digit)

# Count up each digit
counts = []
for i in range (0, 9):
    counts.append(0)

for d in digits:
    counts[d] += 1

# Largest count of a single digit
greatest = -1
for c in counts:
    if c > greatest:
        greatest = c

# Count the number of modes in the data
modes = 0
for c in counts:
    if c == greatest:
        modes += 1

# Output
if modes == 1:
    print (greatest)
else:
    print ("Data was multimodal")


