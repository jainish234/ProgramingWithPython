# 13) Accept the number from the user; display the table of that number.

num = float(input("Enter an integer: "))
print("Multiplication table of:",num)
for i in range(1, 11):
    print(num, 'x', i, '=', num * i)

output:=
Enter an integer: 9.6
Multiplication table of: 9.6
9.6 x 1 = 9.6
9.6 x 2 = 19.2
9.6 x 3 = 28.799999999999997
9.6 x 4 = 38.4
9.6 x 5 = 48.0
9.6 x 6 = 57.599999999999994
9.6 x 7 = 67.2
9.6 x 8 = 76.8
9.6 x 9 = 86.39999999999999
9.6 x 10 = 96.0