#15) Create an empty dictionary, Insert some Roll:Name into it. i). Retrieve 5th value using key, ii). Retrieve all the roll numbers, iii). Retrieve all the names, iv). Change the name of the student having roll no. 7, v). Remove roll no 9, vi). Display the dictionary.

a={}
print(a)
a[1]='abc'
a[2]='fjds'
a[3]='ytryuf'
a[4]='dfc'
a[5]='edf'
a[6]='wsd'
a[7]='gvb'
a[8]='tgh'
a[9]='tgh'
a[10]='yhj'
print(a)
#retrieve 5 th value using key
print(a[5])
#retrieve all the roll number
print(a.keys())
#retrieve all the names
print(a.values())
#change the name of the student having roll no. 7
a[7]='gvb'
print(a)
#remove roll no 9
del a[9]
#display the dictionary
print(a)

#output:=

{}
{1: 'abc', 2: 'fjds', 3: 'ytryuf', 4: 'dfc', 5: 'edf', 6: 'wsd', 7: 'gvb', 8: 'tgh', 9: 'tgh', 10: 'yhj'}
edf
dict_keys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
dict_values(['abc', 'fjds', 'ytryuf', 'dfc', 'edf', 'wsd', 'gvb', 'tgh', 'tgh', 'yhj'])
{1: 'abc', 2: 'fjds', 3: 'ytryuf', 4: 'dfc', 5: 'edf', 6: 'wsd', 7: 'gvb', 8: 'tgh', 9: 'tgh', 10: 'yhj'}
{1: 'abc', 2: 'fjds', 3: 'ytryuf', 4: 'dfc', 5: 'edf', 6: 'wsd', 7: 'gvb', 8: 'tgh', 10: 'yhj'}
