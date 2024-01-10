#The distance between two cities is input through keyboard. Write a program to convert and 
#print this distance in feet, meter, inch and centimeter.

distance = float(input("Distance Between Two Cities is:"))

meter = distance * 1000

feet = distance * 3280.8

centimeter = distance * 100000

inches = distance * 39370.07

print("Distance in Meter is:",meter)
print("Distance in Feet is:",feet)
print("Distance in Centimeter is:",centimeter)
print("Distance in Inches is:",inches)

# OP:
# Distance Between Two Cities is:220km
# Distance in Meter is: 220000.0
# Distance in Feet is: 721776.0
# Distance in Centimeter is: 22000000.0
# Distance in Inches is: 8661415.4