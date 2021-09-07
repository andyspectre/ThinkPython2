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

# get the file
with open('user_manuals.txt') as f:
    read_data = f.read()

# get rid of punctuation
for word in read_data:
    if word in string.punctuation:
        read_data = read_data.replace(word, '')

# get rid of whitespaces
for word in read_data:
    if word in string.whitespace:
        read_data = read_data.replace(word, '')

print(read_data.lower())
