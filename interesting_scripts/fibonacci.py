""" Find first n Fibonacci numbers """
def fibonacci(n):
    if not isinstance(n, int):
        raise TypeError()
    elif n < 0:
        raise ValueError()
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(10):
    print(fibonacci(n))
