# Andrea Cocco 2020
# Chapter 11 Exercise 2 from the book:
#     
# Think Python, 2nd Edition
# by Allen Downey
# http://thinkpython2.com
#
# Read the documentation of the dictionary methods setdefault and use it 
# to write a more concise version of invert_dict.

def histogram(string):
    """Counts how many times a letter appears in a string and put them
    into a dictionary. The key is the letter and the value is the number 
    (how many of that letter)
    """

    d = dict()
    for letter in string:
        if letter not in d:
            d[letter] = 1
        else:
            d[letter] += 1
    return d

def invert_dict(d):
    """Given a dictionary that maps a key to a value, returns a new 
    dictionary in which the key is the previous dictionary's value and the value
    is a list containing the previuos dictionary's key(s).
    """
    d2 = dict()
    for key in d:
        val = d[key]
        d2.setdefault(val, []).append(key)
    return d2
        
inverse = invert_dict(hist)
print(inverse)
