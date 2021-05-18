# Andrea Cocco 2020
# Chapter 10 Exercise 10 from the book:
#     
# Think Python, 2nd Edition
# by Allen Downey
# http://thinkpython2.com
#
# Write a function called in_bisect (I have called it 'binary_search' 
# instead) that takes a sorted list and a target value and returns 
# the index of the value in the list if it's there, or None if it's not.

def create_list(f, item):
    myli = []
    i = item
    for lines in f:
        word = lines.strip()
        myli.append(word)
    myli.sort()
    myli
    return binary_search(myli, i)
    
def binary_search(li, item): 
    low = 0
    high = len(li)-1

    while low <= high:
        mid = (low + high) // 2
        guess = li[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return none

fin = open('pass_list.txt')
print(create_list(fin, '102030'))
