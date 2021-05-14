# Andrea Cocco 2020
# Chapter 10 Exercise 4 from the book:
#     
# Think Python, 2nd Edition
# by Allen Downey
# http://thinkpython2.com
#
# Write a function called chop that takes a list, modifies it by 
# removing the first and last elements, and return None.

def chop(li):
    del li[0]
    del li[-1] 
    return li

t = [1, 2, 3, 4, 5, 6, 7]
print(chop(t))
