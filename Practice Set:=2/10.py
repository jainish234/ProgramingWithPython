#10) Create bytearray, enter some values and perform the following: i). Replace the 3rd element with 7, ii). Display the 5th element.
a=[1,2,58,54,7,6]
b=bytearray(a)
print(b)
b[3]=3
print(b)
print(b[5])

#output:=
bytearray(b'\x01\x02:6\x07\x06')
bytearray(b'\x01\x02:\x03\x07\x06')
6