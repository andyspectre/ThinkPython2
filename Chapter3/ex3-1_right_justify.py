# Andrea Cocco 2020
# Chapter 3 Exercise 1 from the book:
# 
# Think Python, 2nd Edition
# by Allen Downey
# http://thinkpython2.com
# 
# Write a function named right_justify that takes a string names s as a 
# parameter and prints the string with enough leading spaces so that the
# last letter of the string is in column 70 of the display:

def right_justify(s):
    spaces = 70-len(s)
    just = ' '*spaces+s 
    print(just)

right_justify('python')
