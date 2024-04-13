# (12.) Accept dimension of the array and its values from the user, create an array as desired.

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

array = []

print("Enter values for the array:")
for i in range(rows):
    row = []
    for j in range(cols):
        value = input("Enter value for position ({}, {}): ".format(i, j))
        row.append(value)
    array.append(row)

print("Array:")
for row in array:
    print(row)

#output:=
Enter the number of rows: 2
Enter the number of columns: 4
Enter values for the array:
Enter value for position (0, 0): 2
Enter value for position (0, 1): 5
Enter value for position (0, 2): 6
Enter value for position (0, 3): 7
Enter value for position (1, 0): 8
Enter value for position (1, 1): 9
Enter value for position (1, 2): 8 
Enter value for position (1, 3): 5
Array:
['2', '5', '6', '7']
['8', '9', '8', '5']