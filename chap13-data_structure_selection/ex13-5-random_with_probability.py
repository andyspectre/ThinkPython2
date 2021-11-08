import random
from collections import Counter

def histogram(string):

    cnt = Counter()
    for letter in string:
        cnt[letter] += 1

    l = list(cnt)    # unique letters
    v = list(cnt.values())
    for i in random.choices(l,v,k=1):
        return i # random.choices(l, v, k=1)

string = "abracadabra"
result = histogram(string)
print(result)
# test1
