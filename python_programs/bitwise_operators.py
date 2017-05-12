print 5 >> 4  # Right Shift
print 5 << 1  # Left Shift
print 8 & 5   # Bitwise AND
print 9 | 4   # Bitwise OR
print 12 ^ 42 # Bitwise XOR
print ~88     # Bitwise NOT
print 

print 0b1,    #1
print 0b10,   #2
print 0b11,   #3
print 0b100,  #4
print 0b101,  #5
print 0b110,  #6
print 0b111   #7
print "******"
print 0b1 + 0b11
print 0b11 * 0b11
print 

#some binary values
one = 0b1
two = 0b10
three = 0b11
four = 0b100
five = 0b101
six = 0b110
seven = 0b111
eight = 0b1000
nine = 0b1001
ten = 0b1010
eleven = 0b1011
twelve = 0b1100
print 

#conversion of integer to binary
print bin(1)
print bin(1234565776)
#print bin(float(123.7654))
print 

#conversion of binary to integer
print int('0b1001011101', 2)
print int(bin(605), 2)
print 

#shifting // (left shifting and right shifting)
shift_right = 0b1100
shift_left = 0b1
shift_right = shift_right >> 2
shift_left = shift_left << 2
print bin(shift_right)
print bin(shift_left)
print 

#A bit of this 'and' that
print 0b101011110 & 0b100011010
print bin(0b101011110 & 0b100011010)
print int(bin(0b101011110 & 0b100011010), 2)
print bin(int(bin(0b101011110 & 0b100011010), 2))
print 

#A bit of this 'or' that
print 0b101011110 or 0b100011010
print 0b101011110 | 0b100011010
print bin(0b101011110 or 0b100011010)
#print int(bin(0b101011110 | 0b100011010), 3)
print int(bin(0b101011110 | 0b100011010), 2)
print 

#A bit of this 'xor' that
print 0b11010001101101 ^ 0b101101011010100
#print 0b11010001101101 XOR 0b101101011010100
print bin(0b11010001101101 ^ 0b101101011010100)
print int(bin(0b11010001101101 ^ 0b101101011010100), 2)
print bin(int(bin(0b11010001101101 ^ 0b101101011010100), 2))
print 

#A bit of 'not/~' to 'this'
print ~1
print ~2
print ~3
print ~42
print ~123
print ~(int('10101011101010111000001', 2))
print

#complicated operations
def check_bit4(input):
    if 0b1000 & input > 0:
        return 'on'
    else:
        return 'off'
        
print check_bit4(0b1001)
print check_bit4(0b0110)
print 

def third_bit(input):
	desired = 0b100 | input
	if desired > 0:
		return bin(desired)
	else:
		'off'

print third_bit(0b1001000)
print

a = 0b11101110
desired = 0b11111111 ^ a
print bin(desired)
print 

def flip_bit(number, n):
    mask = 0b1 << n-1
    result = bin(number ^ mask)
    return result

print flip_bit(123, 4)
print flip_bit(196482, 324)
print 

