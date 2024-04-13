# (13.) Create a function to calculate the simple interest.

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in percentage): "))
time = float(input("Enter the time period (in years): "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest:", simple_interest)

# output:=
Enter the principal amount: 700
Enter the rate of interest (in percentage): 60
Enter the time period (in years): 4
Simple Interest: 1680.0