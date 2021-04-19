#! usr/bin/env python3

def gcd(a, b):
    """Compute the greatest common divisor of a and b"""
    r = a % b # Remainder
    if r == 0: # if remainder is 0, then b is the GCM
        return b
    else: # if remainder is not 0, divide b by the remainder 
        a = b
        b = r
        return gcd(a, b)

def quit():
    """Prompt user to choose to quit or not"""
    q = input('Do you want to quit? [y/n]')
    if q == 'y':
        print('Goodbye')
    else:
        ask_user()

def ask_user():
    """Prompt user to insert values"""
    val1 = input('Insert first number: ') 
    val1 = int(val1)
    val2 = input('Insert second number: ')
    val2 = int(val2)
    print(gcd(val1, val2))
    quit()

ask_user()
