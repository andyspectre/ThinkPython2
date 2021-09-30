""" Compute the factorial of a positive integer """

def factorial(n):
    if not isinstance(n, int):
        raise TypeError()
    elif n < 0:
        raise ValueError()
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

a = -6 
b = 2.5
c = 4
print(factorial(b))
