def CountBits(x):
    num_bits = 0

    while x:
        print(str(x) + " : " +str(x & 1))
        num_bits += x & 1
        x >>= 1
        
    return num_bits



print("Total Bits : " + str(CountBits(10)))