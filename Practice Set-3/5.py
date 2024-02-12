# 5. Income Tax department wants to make an application that calculates tax on the basis of the
# income. Accept yearly income earned by the taxpayer as an input and calculate tax to be paid.
# The tax slab is as below:
# Income up to 8 lakhs – No tax
# Income more than 8 lakh and less than 10 lakhs – 15% of income
# Income more than 10 lakhs and less than 20 lakhs – 20% of income
# Income more than 20 lakhs – 30% of income

income = float(input("Enter yearly income in lakhs: "))
slab_1_limit = 8 # Up to 8 lakhs
slab_2_limit = 10 # More than 8 lakhs and less than 10 lakhs
slab_3_limit = 20 # More than 10 lakhs and less than 20 lakhs
if income <= slab_1_limit:
    tax = 0
elif income <= slab_2_limit:
    tax = 0.15 * income
elif income <= slab_3_limit:
    tax = 0.20 * income
else:
    tax = 0.30 * income
print(f"Income: {income} lakhs")
print(f"Tax to be paid: {tax} lakhs")

#output:=
Enter yearly income in lakhs: 14000
Income: 14000.0 lakhs
Tax to be paid: 4200.0 lakhs