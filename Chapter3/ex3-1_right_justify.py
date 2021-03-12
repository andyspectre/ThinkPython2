"""Andrea Cocco 2020
Chapter 3 Exercise 2 from the book:

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Write a function named right_justify that takes a string named s as a parameter and prints the string 
with enough leading spaces so that the last letter of the string is in column 70 of the display:

>>> right_justify('monty')
                                                                 monty

Hint: Use string concatenation and repetition. Also, Python provides a built-in function called len 
that returns the length of a string, so the value of len('monty') is 5.
"""

def right_justify(s):
    spaces = 70-len(s)
    just = ' '*spaces+s 
    print(just)

right_justify('python')
