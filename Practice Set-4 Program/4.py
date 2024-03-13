# 4) Accept one integer value from the user; display the length of the entered number, also display
# that the entered number is of four digits or not.

# Accept input from the user
num = int(input("Enter an integer: "))

# Calculate the length of the entered number
num_length = len(str(num))

# Display the length of the entered number
print("Length of the entered number:", num_length)

# Check if the entered number is four digits or not
if num_length == 4:
    print("The entered number is of four digits.")
else:
    print("The entered number is not of four digits.")

output:=
Enter an integer: 6
Length of the entered number: 1
The entered number is not of four digits.
