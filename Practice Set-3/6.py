# 6. Accept two integer values in separate variable, display the small value and big value out of it.

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

smaller=''
larger=''

if num1 < num2:
    smaller, larger = num1, num2
else:
    smaller, larger = num2, num1

print("Larger Value: ",larger)
print("Smaller Value:",smaller)

#output:=
Enter the first integer: 90
Enter the second integer: 80
Larger Value:  90
Smaller Value: 80