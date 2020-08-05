def bits_clear(value):
    mask = 0b00000000
    return bin(value & mask)

def set_bits(value):
    mask = 0b11111111
    return bin(value | mask)

def even_bits(value):
    mask = 0b1010101
    return bin(value | mask)

def bits_flip(value):
    mask = 0b11110000
    return bin(mask ^ value)

def bits_allFlip(value):
    mask = 0b11111111
    return bin(value ^ mask)

def main():
    val = int(input('Enter binary: '), 2)
    print(bits_clear(val))
    print(set_bits(val))
    print(even_bits(val))
    print(bits_allFlip(val))

main()