# Andrea Cocco 2022
# Chapter l4 Exercise 2 from the book:
#     
# Think Python, 2nd Edition
# by Allen Downey
# http://thinkpython2.com
#

import anagrams

with open("names.txt") as f:
    print(anagrams.create_list(f))
