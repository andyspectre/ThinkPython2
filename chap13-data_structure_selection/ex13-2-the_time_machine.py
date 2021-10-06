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
from operator import itemgetter
from collections import Counter

with open("test.txt", encoding="UTF-8") as f:
    strippables = string.punctuation + string.whitespace
    cnt = Counter()
    for line in f:
        for word in line.split():
            word = word.strip(strippables).lower()
            cnt[word] += 1

    words_total = (sum(cnt.values()))


    print("Total number of words: ", words_total)
    print("Total number of different words: ", len(list(cnt)))
    print()
    print("Most common 3 words: ")

    for word, freq in(cnt.most_common(3)):
        print(f"{word:15} ==> {freq:5}")
    
    print()
    print("Word frequency:")
    
    for word, freq in sorted(cnt.items(), key=itemgetter(1), reverse=True):
        print(f"{word:15} ==> {freq:5}")
