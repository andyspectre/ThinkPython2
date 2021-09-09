# Andrea Cocco 2020
# Chapter 13 Exercise 2 from the book:
#     
# Think Python, 2nd Edition
# by Allen Downey
# http://thinkpythimport string

"""Go to Project Gutenberg and download your favorite out-of-copyright
book in plain text format. Modify your program from the previous exercise
to read the book you downloaded, skip over the header information at the
beginning of the file, and process the rest of the words as before.
Then modify the program to count the total number of words in the book,
and the number of times each word is used. Print the number of 
different words used in the book.
"""
import string

with open('test.txt', encoding='UTF-8') as f:
    strippables = string.punctuation + string.whitespace
    hist = {}    # histogram to track words frequency  

    # replace hypens with spaces
    for line in f:
        line = line.replace('-', ' ')

        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()
            # print(word)
            if word not in hist:
                hist[word] = 1
            else:
                hist[word] += 1
    print(hist)
