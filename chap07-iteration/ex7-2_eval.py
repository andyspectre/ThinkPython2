# Andrea Cocco 2020
# Chapter 7 Exercise 2 from the book:
#     
# Think Python, 2nd Edition
# by Allen Downey
# http://thinkpython2.com
#
# Write a function called eval_loop that iteratively
# prompts the user, takes the resulting input and evaluates
# it using eval, and prints the result. It should continue until the user enters 'done'.

def ask_user():
    val = input('Insert a value, enter "done" to exit: ')
    if val != 'done':
        print(eval(val))
        ask_user()

ask_user()
