#7. Accept marks from 4 students, display which mark is highest among all.

marks_list = []
for i in range(4):
    marks = float(input(f"Enter marks for Student {i + 1}: "))
    marks_list.append(marks)
highest_mark = max(marks_list)
print(f"Highest mark among all students: {highest_mark}")

#output:=
Enter marks for Student 1: 80
Enter marks for Student 2: 70
Enter marks for Student 3: 90
Enter marks for Student 4: 60
Highest mark among all students: 90.0