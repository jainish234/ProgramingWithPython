3.Accept one integer value from the user; check whether entered number is between 0-100 or not.

# Accept input from the user
num = int(input("Enter an integer: "))

# Check if the entered number is between 0 and 100
if num >= 0 and num <= 100:
    print("The entered number is between 0 and 100.")
else:
    print("The entered number is not between 0 and 100.")

output:=
Enter an integer: 900
The entered number is not between 0 and 100.