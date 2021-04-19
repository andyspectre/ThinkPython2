# Andrea Cocco 2020
# Chapter 6 Exercise 2 from the book:
#     
# Think Python, 2nd Edition
# by Allen Downey
# http://thinkpython2.com

# Write a function named ack that evaluates the Ackermann function.
# Use your function to evaluate ack(3, 4), which should be 125.
# What happens for larger values of m and n?

def ack(m, n):
    """Computes the Ackermann function
    n, m: non-negative integers"""

    if not isinstance(m, int):
        print('Ackermann function is defined for non-negative integers values')
        return None
    elif not isinstance(n, int):
        print('Ackermann function is defined for non-negative integers values')
        return None
    elif m < 0 or n < 0:
        print('Ackermann function is not defined for negative integers')
        return None
    elif m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m-1, 1)
    elif m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))



def ask_values():
    """Prompt the user to enter the values"""
    x = input('Insert first non-negative integer and press enter: ')
    y = input('Insert second non-negative integer and press enter: ')
    x = int(x)
    y = int(y)
    print(ack(x, y))
    quit()

def quit():
    """Prompt the user for action: quit or not?"""
    quit = input('Do you want to quit? y/n ')
    if quit == 'y':
        print('Goodbye!')
    else: 
        ask_values()

ask_values()

