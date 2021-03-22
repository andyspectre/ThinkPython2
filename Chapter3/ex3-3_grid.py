# Andrea Cocco 2020
# Chapter 3 Exercise 3 of the book:
# Think Python, 2nd Edition
# by Allen Downey
# http://thinkpython2.com
#
# Note: This exercise should be done using only the statements
# and other features we have learned so far.

# Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +

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
