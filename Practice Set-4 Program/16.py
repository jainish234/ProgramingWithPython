# 16) Accept numbers from the user; find and display number of zeros available in the number.

# Accept a number from the user
num = input("Enter a number: ")

# Initialize a counter for zeros
zero_count = 0

# Iterate through each digit in the number
for digit in num:
    if digit == '0':
        zero_count += 1

# Display the number of zeros in the number
print("Number of zeros in the number:", zero_count)

output:=
Enter a number: 9808760870
Number of zeros in the number: 3