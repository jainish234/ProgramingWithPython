# 11) Display the following output using loop:
# i. 1 to 10
# ii. 10 to 1
# iii. 1 3 5 7 9
# iv. 2 4 6 8 10

# i. 1 to 10
print("i. 1 to 10:")
for i in range(1, 11):
    print(i, end=" ")
print("\n")

# ii. 10 to 1
print("ii. 10 to 1:")
for i in range(10, 0, -1):
    print(i, end=" ")
print("\n")

# iii. 1 3 5 7 9
print("iii. 1 3 5 7 9:")
for i in range(1, 10, 2):
    print(i, end=" ")
print("\n")

# iv. 2 4 6 8 10
print("iv. 2 4 6 8 10:")
for i in range(2, 11, 2):
    print(i, end=" ")
print("\n")

output:=
i. 1 to 10:
1 2 3 4 5 6 7 8 9 10 

ii. 10 to 1:
10 9 8 7 6 5 4 3 2 1

iii. 1 3 5 7 9:
1 3 5 7 9

iv. 2 4 6 8 10:
2 4 6 8 10
