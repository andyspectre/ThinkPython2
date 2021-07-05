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
    r = []
    for key in d:
        if len(d[key]) > 1:
            r.append(d[key])
    return r

def key_getter(strs):
    key = [0] * 26
    for letter in strs:
        if letter.islower():
            start = ord('a')
        elif letter.isupper():
            start = ord('A')
        position = ord(letter) - start
        key[position] += 1
    key = tuple(key)
    return key

def create_list(strs):
    li = []
    d = dict()
    for line in strs:
        word = line.strip()
        li.append(word)
    for word in li:
        key = key_getter(word)
        if key not in d:
            d[key] = [word]
        else:
            d[key].append(word)
    return result(d)

fin = open("file.txt")
print(create_list(fin))
