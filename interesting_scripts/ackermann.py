"""Computes the Ackermann function. m, n: non-negative integers """
def ack(m, n):
    if not isinstance(m, int):
        print('Ackermann function is defined for non-negative integers values')
        raise TypeError 
    elif not isinstance(n, int):
        print('Ackermann function is defined for non-negative integers values')
        raise TypeError
    elif m < 0 or n < 0:
        print('Ackermann function is not defined for negative integers')
        raise ValueError 
    elif m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m-1, 1)
    elif m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))

print(ack(4,2))
