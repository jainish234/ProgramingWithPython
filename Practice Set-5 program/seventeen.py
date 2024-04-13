# (17.)Demonstrate the use of: i). break and ii). pass.

# break:=

for num in range(0,10):
    if num == 5:
        break
    print(f'no: {num}')

# output:=
# no: 0
# no: 1
# no: 2
# no: 3
# no: 4

# pass:=

for num in range(0,10):
    if num == 5:
        pass
    print(f'no: {num}')

# output:=
no: 0
no: 1
no: 2
no: 3
no: 4
no: 5
no: 6
no: 7
no: 8
no: 9