# 15) Accept numbers from the user; display the count of the entered numbers.

n=int(input("Enter number:"))
count=0
while(n>0):
    count=count+1
    n=n//10
print("The number of digits in the number are:",count)

output:=
Enter number:67890
The number of digits in the number are: 5