# 3. Rajkot Corporation wants to make simple application to calculate Water Bill of Rajkotians. Water
# is being delivered by the Corporation on per litre charges as below:
# Upto 90 litres – Rs. 0/ltr
# Upto 150 litres – Rs. 2/ltr
# Upto 250 litres – Rs. 5/ltr
# More than 250 – Rs. 10/ltr
# Accept unit consumption from consumer and display the bill amount.

units = int(input("Enter the units consumed: "))
if units < 0:
    print("Units consumed cannot be negative.")
else:
    if units <= 90:
        bill_amount = 0
    elif units <= 150:
         bill_amount = (units - 90) * 2
    elif units <= 250:
        bill_amount = (units - 150) * 5 + 120  # 90 * 0 + 60 * 2
    else:
        bill_amount = (units - 250) * 10 + 370  # 90 * 0 + 60 * 2 + 100 * 5
    print("Water bill amount: Rs.", bill_amount)
print("Please enter a valid integer for units consumed.")

#output:=
Enter the units consumed: 600
Water bill amount: Rs. 3870
Please enter a valid integer for units consumed.