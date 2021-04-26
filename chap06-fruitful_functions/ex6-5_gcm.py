# Andrea Cocco 2020
# Chapter 6 Exercise 5 from the book:
#     
# Think Python, 2nd Edition
# by Allen Downey
# http://thinkpython2.com

# Write a function called gcd that takes parameters a and b
# and returns their greatest common divisor.
# Credit: This exercise is based on an example from Abelson and
# Sussman’s Structure and Interpretation of Computer Programs.

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
