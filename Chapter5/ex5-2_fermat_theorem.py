# Andrea Cocco 2020
# Chapter 5 Exercise 5-2 from the book:
#   
# Think Python, 2nd Edition
# by Allen Downey
# http://thinkpython2.com
# 
# Fermat's Last Theorem says that there are no positive integers a, b, and c such that
# a^n + b^n = c^n 
# for any values of n greater than 2.
# 
# 1.Write a function named check_fermat that takes four parameters-a, b, c and n-and 
# checks to see if Fermat's theorem holds. If n is greater than 2 and
# a^n + b^n = c^n 
# the program should print, "Holy smokes, Fermat was wrong!" 
# Otherwise the program should print, "No, that doesn't work."

# 2.Write a function that prompts the user to input values for a, b, c and n, 
# converts them to integers, and uses check_fermat to check whether they violate Fermat's theorem.


def check_fermat(a,b,c,n):
    """Calculate the nth power of a and b, add them and check if 
    they are equal to the nth power of c.
    a: first integer
    b: second integer
    c: third integer
    n: exponent
    """
    print (a, 'to the power of', n, 'plus', b, end=' ')
    print ('to the power of', n, '=', a**n+b**n)
    print (c, 'to the power of', n, '=', c**n)
    if n > 2 and a**n+b**n == c**n:
        print ('Holy smokes, Fermat was wrong!')
    else:
        print ('No, that doesn\'t work.')

    exit = input('Do you want to exit? y/n\n')
    if exit == 'n':
        mynumbers()
    elif exit == 'y':
        print ('Ciao!')

def mynumbers():
    """Ask user to input three integers and an exponent"""
    print ('Let\'s check if Fermat Last Theorem holds...')
    a = input('Enter the first integer: ')
    a = int(a)
    b = input('Enter the second integer: ')
    b = int(b)
    c = input('Enter the third integer: ')
    c = int(c)
    n = input('Enter the exponent: ')
    n = int(n)
    check_fermat(a,b,c,n)

mynumbers()
