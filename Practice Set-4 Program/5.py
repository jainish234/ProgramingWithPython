# 5) Accept one integer value from the user; display appropriate day of the week.

# Accept input from the user
num = int(input("Enter a number between 1 and 7: "))

# Check if the input number is within the valid range and display the corresponding day of the week

if num == 1:
    print("Monday")
elif num == 2:
    print("Tuesday")
elif num == 3:
    print("Wednesday")
elif num == 4:
    print("Thursday")
elif num == 5:
    print("Friday")
elif num == 6:
    print("Saturday")
elif num == 7:
    print("Sunday")
else:
    print("Invalid input. Please enter a number between 1 and 7.")

output:=
Enter a number between 1 and 7: 4
Thursday