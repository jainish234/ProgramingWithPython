# 8) Accept one integer value from the user; display the table of it.

num = int(input("Enter an integer: "))

# Display the multiplication table
print("Multiplication table of:",num)
for i in range(1, 11):
    print(num, 'x', i, '=', num * i)

output:=
Enter an integer: 9
Multiplication table of: 9
9 * 1 = 9
9 * 2 = 18
9 * 3 = 27
9 * 4 = 36
9 * 5 = 45
9 * 6 = 54
9 * 7 = 63
9 * 8 = 72
9 * 9 = 81
9 * 10 = 90