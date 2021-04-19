#! usr/bin/env python3

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

    
