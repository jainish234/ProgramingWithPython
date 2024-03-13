# 6) Take choice from the user, and perform the arithmetic operation as per the choice.
# Choices: 1) Addition, 2) Subtraction, 3) Multiplication 4) Division

# Accept input from the user for the choice
print("Choices:")
print("1) Addition")
print("2) Subtraction")
print("3) Multiplication")
print("4) Division")
choice = int(input("Enter your choice (1/2/3/4): "))

# Accept two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform arithmetic operations based on the choice
if choice == 1:
    result = num1 + num2
    operation = "Addition"
elif choice == 2:
    result = num1 - num2
    operation = "Subtraction"
elif choice == 3:
    result = num1 * num2
    operation = "Multiplication"
elif choice == 4:
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        result = None
    else:
        result = num1 / num2
        operation = "Division"
else:
    print("Invalid choice.")
    result = None

# Print the result if it's not None
if result is not None:
    print(f"The result of {operation} is:", result)

output:=
Choices:
1) Addition
2) Subtraction
3) Multiplication
4) Division
Enter your choice (1/2/3/4): 2
Enter the first number: 80
Enter the second number: 60
The result of Subtraction is: 20.0