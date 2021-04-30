# Andrea Cocco 2020
# Chapter 8 Exercise 3 from the book:
#     
# Think Python, 2nd Edition
# by Allen Downey
# http://thinkpython2.com
#
# A step size of -1 goes through the word backwards, so the slice [::-1]
# generates a reversed string. Use this idiom to write a one-line 
# version of is_palindrome from Exercise 6-3

def is_palindrome(w):
    return w == w[::-1]

print(is_palindrome('redivider'))
print(is_palindrome('doors'))
print(is_palindrome('civic'))
print(is_palindrome('computers'))
