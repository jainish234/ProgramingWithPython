# (8.) Create a numeric array and perform following operations on it: Add 2 to each elements,
# Subtract 3 from each element, Multiply each element with 3, Divide each element by 2, Find max and min,
# find the average of all elements.

numeric_array = [5, 10, 15, 20, 25]
numeric_array_added = [num + 2 for num in numeric_array]
numeric_array_subtracted = [num - 3 for num in numeric_array]
numeric_array_multiplied = [num * 3 for num in numeric_array]
numeric_array_divided = [num / 2 for num in numeric_array]

maximum = max(numeric_array)
minimum = min(numeric_array)
average = sum(numeric_array) / len(numeric_array)
print("Original array:", numeric_array)
print("Added 2:", numeric_array_added)
print("Subtracted 3:", numeric_array_subtracted)
print("Multiplied by 3:", numeric_array_multiplied)
print("Divided by 2:", numeric_array_divided)
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Average:", average)

# output:=
Original array: [5, 10, 15, 20, 25]
Added 2: [7, 12, 17, 22, 27]
Subtracted 3: [2, 7, 12, 17, 22]
Multiplied by 3: [15, 30, 45, 60, 75]
Divided by 2: [2.5, 5.0, 7.5, 10.0, 12.5]
Maximum: 25
Minimum: 5
Average: 15.0