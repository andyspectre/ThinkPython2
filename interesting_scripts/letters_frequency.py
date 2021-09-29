from operator import itemgetter

def myli(s):
    """Take a string s, call most_frequent(s) to create a dictionary
    and then put the values in an ordered list of tuples.
    """
    words = most_frequent(s)

    # create a key, value list to be iterated over
    pairs = [(v, k) for (k, v) in words.items()]
    
    return sorted(pairs, key=itemgetter(0), reverse=True) 

def most_frequent(s):
    """Take a string s and return a dictionary in which the
    key-value pairs are letter-number where letter is every
    letter in the string and number is how many times that letter
    appears.
    """
    d = dict()
    for letter in s:
        d[letter] = d.get(letter,0) + 1
    return d

s = "Hello I like reading science-fiction books"
frequency = myli(s)
for i in frequency:
    print(i)
