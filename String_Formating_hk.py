#Given an integer, n, print the following values for each integer i from 1 to n:

#1. Decimal
#2. Octal
#3. Hexadecimal (capitalized)
#4. Binary
#The four values must be printed on a single line in the order specified above for each i from 1 to n. 
#Each value should be space-padded to match the width of the binary value of n.

def print_formatted(num) :
    #print()
    i = 1
    w = len((bin(num).lstrip("0b")))
    print(w)
    while i <= num :
        print(str(i).rjust(w), oct(i).lstrip("0o").rjust(w), (hex(i).lstrip("0x")).upper().rjust(w), (bin(i)).lstrip("0b").rjust(w))
        i += 1

n = int(input())
print_formatted(n)