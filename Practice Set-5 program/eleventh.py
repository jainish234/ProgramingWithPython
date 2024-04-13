# (11.) Take two arrays enter 5 digits in both arrays.Compare the corresponding element from each array and
# display only the bigger number.

array1 = []
array2 = []
print("Enter 5 digits for array1:")
for i in range(5):
	digit = int(input("Enter digit {}: ".format(i + 1)))
	array1.append(digit)
print("Enter 5 digits for array2:")
for i in range(5):
	digit = int(input("Enter digit {}: ".format(i + 1)))
	array2.append(digit)
print("Comparing corresponding elements:")
for i in range(5):
	if array1[i] > array2[i]:
		print("Bigger number:", array1[i])
	elif array1[i] < array2[i]:
		print("Bigger number:", array2[i])
	else:
		print("Both numbers are equal at index", i)

# output:=
Enter 5 digits for array1:
Enter digit 1: 23
Enter digit 2: 40
Enter digit 3: 70
Enter digit 4: 60
Enter digit 5: 43
Enter 5 digits for array2:
Enter digit 1: 96
Enter digit 2: 44
Enter digit 3: 33
Enter digit 4: 22
Enter digit 5: 88
Comparing corresponding elements:
Bigger number: 96
Bigger number: 44
Bigger number: 70
Bigger number: 60
Bigger number: 88