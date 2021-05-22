# Andrea Cocco 2020
# Chapter 11 Exercise 1 from the book:
#     
# Think Python, 2nd Edition
# by Allen Downey
# http://thinkpython2.com
#
# Write a function that reads a file with a list of words and stores
# them as keys in a dictionary. It doesn't matter what the values are. 
# Then you can use the in operator as a fast way to check whether a 
# string is in the dictionary.
# 
# For this exercise I have used this list from Daniel Miessler Github:
# https://github.com/danielmiessler/SecLists/blob/master/Passwords/2020-200_most_used_passwords.txt 

def pwd_dict(f):
    d = dict()
    for line in f:
        word = line.strip()
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
    return d


fin = open('pass_list.txt')
popular_passwords = pwd_dict(fin)

your_password = 'password'
if your_password in popular_passwords:
    print(your_password, 'is in the list, you should change it.')
