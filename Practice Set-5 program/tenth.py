# (10.) Accept numeric elements from the user, store it to the array and display. Ask user to enter
# search element. Display the position of the searched element.

numeric_array = []
num_elements = int(input("Enter the number of elements: "))

for i in range(num_elements):
    element = float(input("Enter element {}: ".format(i+1)))
    numeric_array.append(element)

print("Array:", numeric_array)

search_element = float(input("Enter the element to search for: "))

try:
    position = numeric_array.index(search_element)
    print("Position of the search element:", position)
except ValueError:
    print("Search element not found in the array.")


# output:=
Enter the number of elements: 5
Enter element 1: 78
Enter element 2: 89
Enter element 3: 80
Enter element 4: 90
Enter element 5: 56
Array: [78.0, 89.0, 80.0, 90.0, 56.0]
Enter the element to search for: 80
Position of the search element: 2