# 17) Accept an integer from the user; tell user that whether entered number is even or odd.

even_odd = 'Y'

while even_odd.upper() == 'Y':
    num = int(input("Enter the number: "))

    if num % 2 == 0:
        print(num, "is an even number")
    else:
        print(num, "is an odd number")

    even_odd = input("Do you want to check another number? (Y/N): ")

    while even_odd.upper() not in ['Y', 'N']:
        print("Invalid input! Please enter 'Y' or 'N'.")
        even_odd = input("Do you want to check another number? (Y/N): ")

    if even_odd.upper() == 'N':
        break

output:
Enter the number: 7
7 is an odd number
Do you want to check another number? Y
Enter the number: 2
2 is an even number
Do you want to check another number? N