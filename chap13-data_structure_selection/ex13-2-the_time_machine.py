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
    print(type(hist))

    # replace hypens with spaces
    counter = 0
    for line in f:
        line = line.replace('-', ' ')

        for word in line.split():
            counter += 1
            word = word.strip(strippables)
            word = word.lower()
            hist[word] = hist.get(word, 0) + 1

    print('Words frequency:')
    
    # create iterator of (value, key) pairs
    pairs = zip(hist.values(), hist.keys())

    # sort in reverse order and print
    for i in sorted(pairs, reverse=True):
        print(i[0], ':', i[1])

    print('total number of words:', counter)
