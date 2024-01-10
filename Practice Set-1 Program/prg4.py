#Write a program to calculate simple interest.

principle_amount=float(input("Enter the Principle Amount: \n"))
rate=float(input("Enter the Rate Of Interest: \n"))
time=int(input("Enter the Time: \n"))

simple_interest = (principle_amount*rate*time)/100

print("The Simple Interest Is:",simple_interest)

# OP:
# Enter the Principle Amount:
# 1000
# Enter the Rate Of Interest:
# 10
# Enter the Time:
# 2
# The Simple Interest Is: 200.0