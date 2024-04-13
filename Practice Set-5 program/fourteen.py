# (14.) Create a function to perform basic arithmetic operations on the number.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition_result = num1 + num2
print("Addition Result:", addition_result)

subtraction_result = num1 - num2
print("Subtraction Result:", subtraction_result)

multiplication_result = num1 * num2
print("Multiplication Result:", multiplication_result)

if num2 != 0:
	division_result = num1 / num2
	print("Division Result:", division_result)
else:
	print("Cannot divide by zero.")

# output:=
Enter the first number: 60
Enter the second number: 70
Addition Result: 130.0
Subtraction Result: -10.0
Multiplication Result: 4200.0
Division Result: 0.8571428571428571