# (2.) Accept the string from the user; display the message whether the entered string is palindrome
# or not.

my_str = 'iHaVEgOOdday'

# my_str = 'aIbohPhoBiA'

my_str = my_str.casefold()

rev_str = reversed(my_str)

if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")

# output:=
The string is not a palindrome.

   #OR

The string is a palindrome.