# Andrea Cocco 2020
# Chapter 10 Exercise 7 from the book:
#     
# Think Python, 2nd Edition
# by Allen Downey
# http://thinkpython2.com
#
# Write a function called has_duplicates that takes a list and 
# return True if there is any element that appears more than once. 
# It should not modify the original list.

def has_duplicates(li):
    li2 = sorted(li)
    for elem in range(len(li2)-1):
        return li2[elem] == li2[elem+1]

letters = ['a','b','a','c','d','e','e','c','d']
numbers = [1, 2, 3, 4, 1, 2, 5, 6, 7, 3]
letters2 = ['a','b','c','d','e']
numbers2 = [1, 2, 3, 4, 5, 6, 7]

print(has_duplicates(letters))
print(has_duplicates(numbers))
print(has_duplicates(letters2))
print(has_duplicates(numbers2))
   

