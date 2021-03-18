def evaluate_gate (gate, *args):
    if gate == "OR":
        return 1 if (args[0] + args[1]) > 0 else 0
    if gate == "AND":
        return (args[0] * args[1]) % 2
    if gate == "NOT":
        return 1-args[0]
    if gate == "XOR":
        return ((args[0] + args[1]) % 2)
    if gate == "NAND":
        return 1-((args[0] * args[1]) % 2)
    if gate == "NOR":
        return 1-((args[0] + args[1]) % 2)

truth_table = []

def generate_blank_truth_table (ninputs):
    global truth_table
    truth_table = []
    for i in range (2**ninputs):
        arr = []
        for j in range (0, ninputs):
            arr.append (1 if i%(2**(ninputs-j))>=((2**(ninputs-j))/2) else 0)
        arr.append (0)
        truth_table.append (arr)


def print_truth_table ():
    global truth_table
    ninputs = len(truth_table[0])
    headers = ""
    for n in range (ninputs):
        headers += chr(ord("A")+n)
        headers += " | "
    headers += " O"
    print (headers)
    for row in truth_table:
        for element in row:
            print (element, end='   ')
        print ("")

generate_blank_truth_table (5)
print_truth_table()
        

##gate = input ("Enter gate : ").upper()
##input1 = int(input ("Enter input 1 : ")) % 2
##if gate != "NOT":
##    input2 = int (input ("Enter input 2 : ")) % 2
##    print ("Value :", evaluate_gate (gate, input1, input2))
##else:
##    print ("Value :", evaluate_gate (gate, input1))

    
##
