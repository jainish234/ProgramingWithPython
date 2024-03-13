# 12) Print 1 2 4 8 16 32 64 128 256 512 1024

# Initialize the starting value
num = 1

# Print the sequence
for i in range(11):  # Loop 11 times to print 11 numbers
    print(num, end=" ")
    num *= 2  # Multiply by 2 to get the next number in the sequence

output:=
1 2 4 8 16 32 64 128 256 512 1024 