# Andrea Cocco 2020
# Chapter 13 Exercise 1 from the book:
#     
# Think Python, 2nd Edition
# by Allen Downey
# http://thinkpython2.com

"""Write a program that reads a file, breaks each line into words,
strips whitespace and punctuation from the words, and converts them 
to lowercase.
"""

import string

# get the file
with open('test.txt') as f:
    
    # stuff that we want to remove
    strippables = string.punctuation + string.whitespace

    # replace hyphens with spaces
    for line in f:
        line = line.replace('-', ' ')

        # remove punctuation, spaces and convert to lowercase
        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()
            print(word)
