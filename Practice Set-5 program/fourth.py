# (4.)Accept the string from the user; allow user to
# choose from the following options and perform the task
# as per user’s choice. i). Convert to the upper case,
# ii). Convert to the lower case, iii).
# Convert to the swap case, iv). Convert to the title
# case
#Accept input from the user
user_input = input("Enter a string: ")
# Display options to the user
print("Choose an option:")
print("1. Convert to upper case")
print("2. Convert to lower case")
print("3. Convert to swap case")
print("4. Convert to title case")
# Get user's choice
choice = input("Enter your choice (1/2/3/4): ")
# Perform the chosen operation
if choice == "1":
	result = user_input.upper()
elif choice == "2":
	result = user_input.lower()
elif choice == "3":
	result = user_input.swapcase()
elif choice == "4":
	result = user_input.title()
else:
	result = "Invalid choice"
# Display the result
print("Result:", result)

# output:=
Enter a string: ja is the best friend
Choose an option:
1. Convert to upper case
2. Convert to lower case
3. Convert to swap case
4. Convert to title case
Enter your choice (1/2/3/4): 1
Result: JA IS THE BEST FRIEND
Enter a string: hi mahesh good evenig
Choose an option:
1. Convert to upper case
2. Convert to lower case
3. Convert to swap case
4. Convert to title case
Enter your choice (1/2/3/4): 2
Result: hi mahesh good evenig
Enter a string: hi mehesh is good evening
Choose an option:
1. Convert to upper case
2. Convert to lower case
3. Convert to swap case
4. Convert to title case
Enter your choice (1/2/3/4): 3
Result: HI MEHESH IS GOOD EVENING
Enter a string: hi mehesh is good evening
Choose an option:
1. Convert to upper case
2. Convert to lower case
3. Convert to swap case
4. Convert to title case
Enter your choice (1/2/3/4): 4
Result: Hi Mehesh Is Good Evening