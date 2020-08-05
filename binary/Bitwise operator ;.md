# Bitwise operator ;

## 1.Not

The Nor of a binary number is the value obtained by inverting

all the bits in the binary number:

##   AND

```java
bin(0b01110 & 0b10111)


```

Practice : clear all the bits (set all the bits to zero)

```python
def bits_clear(value):
    mask = 0b00000000
    return value & mask
 #could be able to hide all the potisions in the orginal binary number
```

## OR | ()

Practice of the or

Mask

Set the bits

```python
def mask():
   return(bin(0b1100 | 0b1111))
   
    #even position bits flip
   def even_bits(value):
    mask = 0b1010101
    return bin(value | mask)


```



## XOR^

The XOR of a set of operands is 1 if both the operands differ. Exclusive OR.

A B  A XOR b

0  0       0  

0 1       1

1 0      1

1 1  0 

```python
bin(61)
'0b111101'
bin(19)
'0b10011'
bin(0b111101 ^ 0b10011)
'0b101110'

0b11110000
0b00001111
```

```python
def bits_flip(value):
    mask = 0b11110000
    return bin(mask ^ value)
# The first four bits will be flip
```



## Left shift

A logic shift is a bitwise operation that shifts all the bits of its operand.

The left shift performs a multiplication of n by 2^x

```python
for example
n<<x
n =0b1011
x = 2
n<<x = n *2^x
```

## Right shift

n>>x

A logical shift is a bitwise operation that shifts all the bits of its operand

The right shift performs ```a floor division``` of n by 2^x