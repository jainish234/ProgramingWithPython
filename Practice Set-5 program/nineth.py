# (9).Create a numeric array and do the following: append the element, pop the element, insert an element at the
# desired postion, reverse the elements in the array,convert the array to list.

numeric_array = [1, 2, 3, 4, 5]
numeric_array.append(6)
print("After appending:", numeric_array)
popped_element = numeric_array.pop()
print("Popped element:", popped_element)
print("After popping:", numeric_array)
desired_position = 2
element_to_insert = 10
numeric_array.insert(desired_position,element_to_insert)
print("After inserting", element_to_insert, "atposition", desired_position, ":", numeric_array)
numeric_array.reverse()
print("After reversing:", numeric_array)
numeric_list = list(numeric_array)
print("Converted to list:", numeric_list)

#output:=
After appending: [1, 2, 3, 4, 5, 6]
Popped element: 6
After popping: [1, 2, 3, 4, 5]
After inserting 10 at position 2 : [1, 2, 10, 3, 4, 5]
After reversing: [5, 4, 3, 10, 2, 1]
Converted to list: [5, 4, 3, 10, 2, 1]
