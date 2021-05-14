# Andrea Cocco 2020
# Chapter 10 Exercise 6 from the book:
#     
# Think Python, 2nd Edition
# by Allen Downey
# http://thinkpython2.com
#
# Two words are anagrams if you can rearrange the letters from one 
# to spell the other. Write a function called is_anagram that takes 
# two strings and returns True if they are anagrams.

def is_anagram(x, y):
    return sorted(x) == sorted(y)

t = 'slit'
x = 'list'
a = ['I', 'am', 'tired']
b = ['tired', 'are', 'you']

print(is_anagram(t, x))
print(is_anagram(a, b))
