# (15.) Accept multiple strings and store it into the list using function.

def lste(no):
	lst=[]
	for i in range(no):
		lst.append(input('Enter value of string : '))
	print(lst)

no=int(input('Enter number of strings you want to insert : '))
lste(no)

#Output
Enter number of strings you want to insert : 2
Enter value of string : 46
Enter value of string : 89
['46', '89']