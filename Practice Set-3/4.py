# 4. A tuition class owner wants to make a simple application to allocate grade to the 
# students on the basis of marks student have scored. Accept marks from the students.
# Marks more than 90 – A1 grade
# Marks 80 or less than or equal 90 – A grade
# Marks 70 or less than or equal 80 – B1
# Marks 60 or less than or equal 70 – B
# Marks 50 or less than or equal 60 – Can do Better!
# Marks <50 – Need to work hard.

marks = float(input("Enter the marks obtained by the student: "))

grade=''
if marks > 90:
    grade = "A1"
elif marks > 80:
    grade = "A"
elif marks > 70:
    grade = "B1"
elif marks > 60:
    grade = "B"
elif marks > 50:
    grade = "Can do Better!"
else:
    grade = "Need to work hard."

print("\nGrade:",grade)

#output:=
Enter the marks obtained by the student: 89

Grade: A