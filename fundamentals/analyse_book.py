"""
Count total number of words, total number of different words and word frequency in a file. 

Output example:

Total number of words:  166
Total number of different words:  119

Most common 3 words:
druso           ==>     7
per             ==>     5
come            ==>     4

Word frequency:
druso           ==>     7
per             ==>     5
come            ==>     4
e               ==>     4
nel             ==>     4
del             ==>     4
14              ==>     3
ma              ==>     3
[...]
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
