# Andrea Cocco 2020
# Chapter 5 Exercise 3 from the book:
#   
# Think Python, 2nd Edition
# by Allen Downey
# http://thinkpython2.com

# 1. Write a function named is_triangle that takes three
# integers as arguments, and that prints either "Yes" or "No", depending
# on whether you can or cannot form a triangle from sticks with the
# given lengths.
# 2. Write a function that prompts the user to input three stick
# lengths, converts them to integers, and uses is_triangle to
# check whether sticks with the given lengths can form a triangle.


def is_triangle(a,b,c):
    """Check if, given the lenght of three segments a, b, c, 
    we can can create a triangle.     
    """
    # The sum of two segments has to be greater than or equal to the third
    if a+b < c or a+c < b or b+c < a: 
        print ('No')
    elif a+b == c or a+c == b or b+c == a:
        print ('You can form a "degenerate" triangle.')
    else:
        print ('Yes')
    exitway()

def exitway():
    """Prompt the user for action: exit or continue"""
    exit = input('Do you want to exit? y/n\n')
    if exit == 'n':
        asktriangle()
    elif exit == 'y':
        print('Goodbye!')
    else:
        exitway()

def asktriangle():
    """Prompt the user to enter the lenght of the three segments"""
    print('Let\'s see if we can form a triangle...')
    a = input('Enter the first segment lenght: ')
    a = int(a)
    b = input('Enter the second segment lenght: ')
    b = int(b)
    c = input('Enter the third segment lenght: ')
    c = int(c)
    is_triangle(a,b,c)

asktriangle()

    
