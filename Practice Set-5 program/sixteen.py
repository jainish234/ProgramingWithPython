# (16.)Find the biggest number from three values using lambda.

def big_in_three(*args):
    return sorted(args, key=lambda x: x)[-1]
 
# Example usage
num1 = 10
num2 = 25
num3 = 15
 
result = big_in_three(num1, num2, num3)
print(f"Maximum Number: {result}")

# output:=
Maximum Number: 25