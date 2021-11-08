# Andrea Cocco 2020
# Chapter 13 Exercise 5 from the book:
#     
# Think Python, 2nd Edition
# by Allen Downey
# http://thinkpython2.com

import random
from collections import Counter

def histogram(string):

    cnt = Counter()
    for letter in string:
        cnt[letter] += 1

    l = list(cnt)    # unique letters
    v = list(cnt.values())    # letters frequency
    for i in random.choices(l,weights=v,k=1):
        return i

string = "abracadabra"
cnt = Counter()

# try a 100 times and see if the outcome matches more or less the probability
for i in range(100):
    cnt[histogram(string)]+=1

print(cnt)
