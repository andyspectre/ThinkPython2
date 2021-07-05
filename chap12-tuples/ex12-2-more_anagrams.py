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

def key_getter(strs):
    key = [] 
    for letter in strs:
        if letter.islower():
            start = ord('a')
        elif letter.isupper():
            start = ord('A')
        position = ord(letter) - start
        key.append(position)
    return tuple(key)


def create_list(strs):
    li = []
    for line in strs:
        word = line.strip()
        li.append(word)
    # return li



fin = open("little_anagram_list.txt")
print(key_getter('tea'))
