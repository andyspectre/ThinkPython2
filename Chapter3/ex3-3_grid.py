"""Andrea Cocco 2020
Chapter 3 Exercise 3 from the book:

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Note: This exercise should be done using only the statements and other features we have learned so far.

    1. Write a function that draws a grid like the following:

    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +

    Hint: to print more than one value on a line, you can print a comma-separated sequence of values:

    print('+', '-')

    By default, print advances to the next line, but you can override that behavior and put a space at the end, like this:

    print('+', end=' ')
    print('-')

    The output of these statements is '+ -' on the same line. The output from the next print statement would begin on the next line.
    """
    
    def do_twice(f):
    f()
    f()

def plus_row():
    print('+','- '*4, end='')
    print('+','- '*4, end='')
    print('+')

def pipe_row():
    print('|','  '*3,' |',end=' ')
    print('  '*3, ' |')
    print('|','  '*3,' |',end=' ')
    print('  '*3, ' |')

def print_grid():
    plus_row()
    do_twice(pipe_row)
    plus_row()
    do_twice(pipe_row)
    plus_row()

print_grid()
