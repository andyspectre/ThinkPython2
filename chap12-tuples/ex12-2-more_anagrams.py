""" 1. Read file and initialize a list of strings with it
    2. key_getter(word)
        for each letter of the word:
            get its equivalent unicode number 
            put it in a tuple called key
    3. more_anagrams(tuple, word):
           initialize dictionary
           if tuple is not in dictionary:
               key is the tuple and value is word
           else:
               add word to that key
        key = tuple with numeric representation of the letters of the strings
        value = list of words that match that key
"""
import string

def result(d):
    """ Return a list of words that are anagrams """
    r = []
    for key in d:
        # we want only the elements in the dictionary that have at least
        # two words, that is they are anagrams
        if len(d[key]) > 1:
            r.append(d[key])
    return r

def key_getter(strs):
    """ Return a tuple of "markers" that mark which letters
    appear in a string. These markers will be the keyes of a dictionary
    """
    key = [0] * 26    # initialize a list of 26 "0" (our markers)
    for letter in strs:
        # get the unicode representation of the letters of the words
        if letter.islower():
            start = ord('a')
        elif letter.isupper():
            start = ord('A')
        position = ord(letter) - start

        key[position] += 1    # mark the letters (just add '1' in the list)

    # convert list into tuple so that can be used as key in a dictionary
    key = tuple(key)    
    return key

def anagram(li):
    """ Accept a list of strings as argument and return a dictionary 
    in which the key is a tuple of "markers" representing the letters 
    of the words and the value is the actual word.
    """
    d = dict()

    for word in li:
        key = key_getter(word)
        if key not in d:
            d[key] = [word]
        else:
            d[key].append(word)
    return result(d)

def create_list(strs):
    """ Accept a file with one string per line and return a list
    of strings.
    """
    li = []
    for line in strs:
        word = line.strip()
        li.append(word)
    return anagram(li)


fin = open("pass_list.txt")
print(create_list(fin))
