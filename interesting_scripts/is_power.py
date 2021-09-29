"""Check if a is a power of b"""
def is_power(a, b):
    if  a > b:
        if a%b == 0:
            c = a/b 
            return is_power(c, b)
        else:
            return a%b == 0 # base case
    else:
        return a == b # base case 

print(is_power(81, 3))
print(is_power(82, 3))
print(is_power(91, 3))
print(is_power(125, 5))
