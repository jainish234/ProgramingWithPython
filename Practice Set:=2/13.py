#13) Create a set insert some values. i). Add elements to it and display, ii). Remove elements from it and display.
a={2,6,5,85,85,623,85,2,1,6}
print(a)
a.update([45,12])
print(a)
a.remove(623)
print(a)

#output:=
{1, 2, 5, 6, 85, 623}
{1, 2, 5, 6, 85, 12, 45, 623}
{1, 2, 5, 6, 85, 12, 45}