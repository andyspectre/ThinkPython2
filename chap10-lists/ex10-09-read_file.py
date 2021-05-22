# Andrea Cocco 2020
# Chapter 10 Exercise 9 from the book:
#     
# Think Python, 2nd Edition
# by Allen Downey
# http://thinkpython2.com
#
# Write a function that reads a txt file and builds a 
# list with one element per word. 
#
# For this exercise I have used this list from Daniel Miessler Github:
# https://github.com/danielmiessler/SecLists/blob/master/Passwords/2020-200_most_used_passwords.txt 

def mylist(f):
    myli = []
    for line in f:
        word = line.strip()
        myli.append(word) 
    return myli


fin = open('pass_list.txt')
print(mylist(fin))
