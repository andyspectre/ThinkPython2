# Andrea Cocco 2020
# Chapter 12 Exercise 2 from the book:
#     
# Think Python, 2nd Edition
# by Allen Downey
# http://thinkpython2.com
#
# *******************************************
# Get a list of anagrams from a list of words 
# *******************************************

import string

def result(d):
    # Return a list of words that are anagrams
    r = []
    for v in d.values():
        # we want only the elements in the dictionary that have at least
        # two words, that is they are anagrams
        if len(v) > 1:
            r.append((len(v),v))
    r.sort()

    for i in r:
        print(i)

  # -----------------------------------------
  # Alternative method instead of signature()
  # -----------------------------------------
  #  def key_getter(strs):
  #  # Return a tuple of "markers" that mark which letters
  #  # appear in a string. These markers will be the keyes of a dictionary
  #  key = [0] * 26    # Todo: fix magic constant: 26 
  #  for letter in strs:
  #      # get the unicode representation of the letters of the words
  #      if letter.islower():
  #          start = ord('a')
  #      elif letter.isupper():
  #          start = ord('A')
  #      position = ord(letter) - start
  #      key[position] += 1    # mark the letters (just add '1' in the list)
  #  # convert list into tuple so that can be used as key in a dictionary
  #  key = tuple(key)    
  #  return key

def signature(w):
    t = sorted(w)
    t = ''.join(t)
    return t

def anagram(li):
    # Accept a list of strings as argument and return a dictionary 
    # in which the key is a tuple of "markers" representing the letters 
    # of the words and the value is the actual word.

    d = dict()

    for word in li:
        # key = key_getter(word)
        w = signature(word) 

        if w not in d:
            d[w] = [word]
        else:
            d[w].append(word)

    return result(d)

def create_list(f):
    # Accept a file with one string per line and return a list
    # of strings.

    # dict to get rid of punctuation with translate
    d = dict()
    for i in string.punctuation:
        d[i] = ''

    table = str.maketrans(d)
    li = []
    for line in f:
        for word in line.split():
            word = word.translate(table)
            li.append(word)
    return anagram(li)

if __name__ == '__main__':

    with open("names.txt", encoding="UTF-8") as f:
        create_list(f)
