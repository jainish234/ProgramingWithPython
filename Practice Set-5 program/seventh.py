# (7.) Create a dictionary named library with following keys (Bookid, Title, Author, Price, Publisher).
# a. Display the dictionary, b. Display the name of Author, c. Display the Bookid
# d. Display the length of the dictionary, e. Update the price, f. Insert year as the new key
# and display the dictionary again.

# Create the dictionary
library = {
    'Bookid': '001',
    'Title': 'Python Programming',
    'Author': 'John Smith',
    'Price': 29.99,
    'Publisher': 'ABC Publications'
}

print("Library Dictionary:")
print(library)

print("\nAuthor:", library['Author'])

print("Bookid:", library['Bookid'])

print("Length of the Dictionary:", len(library))

library['Price'] = 34.99

library['Year'] = 2024

print("\nUpdated Library Dictionary:")
print(library)

# output:=
Library Dictionary:
{'Bookid': '001', 'Title': 'Python Programming', 'Author': 'John Smith', 'Price': 29.99, 'Publisher': 'ABC Publications'}

Author: John Smith
Bookid: 001
Length of the Dictionary: 5

Updated Library Dictionary:
{'Bookid': '001', 'Title': 'Python Programming', 'Author': 'John Smith', 'Price': 34.99, 'Publisher': 'ABC Publications', 'Year': 2024}