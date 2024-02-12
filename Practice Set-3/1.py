# 1. Get the basic salary from the employee and display the net salary by calculating the following
# conditions: Applicable TA 4%, DA 30%, HRA 15% on basic salary. Applicable 3% tax, 12% PF on
# basic salary.

basic_salary=int(input("Enter the basic salary:"))
ta=4*basic_salary
da=30*basic_salary
hra=15*basic_salary
net_salary=basic_salary+ta+da+hra
print("Net Salary = ",net_salary)

#output:=
# Enter the basic salary:3600
# Net Salary =  180000