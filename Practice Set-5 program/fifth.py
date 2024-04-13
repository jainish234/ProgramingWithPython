# (5.)Allow users to enter multiple strings in the list;
# arrange the entered string into alphabetical order and
# display.

input_string = input("Enter multiple strings separated by spaces: ")
strings_list = input_string.split()
sorted_list = sorted(strings_list)
print("Sorted strings:")
for string in sorted_list:
print(string)

# output:=
Enter multiple strings separated by spaces: the more
that you read,things you will know.
Sorted strings:
know.
more
read,things
that
the
will
you
you