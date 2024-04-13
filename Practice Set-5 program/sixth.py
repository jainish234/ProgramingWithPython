# (6.) Create a tuple and display it. Enter 25 at the third position and display it again.

my_tuple = (1, 2, 3, 4, 5)

tuple_list = list(my_tuple)

tuple_list.insert(2, 25)

modified_tuple = tuple(tuple_list)

print("Modified Tuple:", modified_tuple)

# output:=
Modified Tuple: (1, 2, 25, 3, 4, 5)
