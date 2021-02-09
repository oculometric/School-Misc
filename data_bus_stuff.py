# Scenario 1
def scen_1 ():
    word_size = int (input ("Enter the data bus width in BYTES: "))
    address_space_size = int (input ("Enter the address bus width in BITS: "))
    words_addressable = 2**address_space_size
    bytes_addressable = (2**address_space_size)*word_size
    print ("The number of accessible memory locations is", words_addressable, "these could be bytes or words depending on the address system.")
    print ("In a byte-addressable system, this means there are", words_addressable, "bytes of memory addressable:", (words_addressable/(1024)), "kB,", (words_addressable/(1024*1024)), "MB,", (words_addressable/(1024*1024*1024)), "GB")
    print ("In a word-addressable system, this means there are", bytes_addressable, "bytes of memory addressable:", (bytes_addressable/(1024)), "kB,", (bytes_addressable/(1024*1024)), "MB,", (bytes_addressable/(1024*1024*1024)), "GB")

# Scenario 2
def scen_2 ():
    capacity_bytes = int (input ("Enter the amount of RAM capacity in BYTES: "))
    word_sizes = [8, 16, 32, 64]
    for word_size in word_sizes:
        address_bus_bits = 1
        while ((2**address_bus_bits)/(word_size/8) < capacity_bytes):
            address_bus_bits += 1
        print ("For a data bus width of", word_size, "the address bus would have to be", address_bus_bits, "bits wide")

scen_2()
