# Andrea Cocco 2020
# Chapter 10 Exercise 5 from the book:
#     
# Think Python, 2nd Edition
# by Allen Downey
# http://thinkpython2.com
#
# Two words are anagrams if you can rearrange the letters from one 
# to spell the other. Write a function called is_anagram that takes 
# two strings and returns True if they are anagrams.

def is_sorted(li):
    return li == sorted(li)

t = [1, 2, 3, 4, 5, 6, 7]
x = ['a', 'c', 'b', 'd']
print(is_sorted(t))
print(is_sorted(x))
