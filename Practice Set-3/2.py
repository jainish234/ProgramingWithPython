# 2. Get the marks of 5 subjects at the command line and display the total of marks, and percentage.

import sys

if len(sys.argv) != 6:
    sys.exit(1)

marks = [float(arg) for arg in sys.argv[1:]]

total_marks = sum(marks)
total_subjects = len(marks)
percentage = (total_marks / (total_subjects * 100)) * 100

print("\nTotal Marks: ", total_marks)
print("Percentage: {:.2f}%".format(percentage))

#output:=
PS D:\JMB Practice Set-3> python 2.py 70 80 90 60 70
Total Marks:  370.0
Percentage: 74.00%
