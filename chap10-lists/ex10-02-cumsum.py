# Andrea Cocco 2020
# Chapter 10 Exercise 2 from the book:
#     
# Think Python, 2nd Edition
# by Allen Downey
# http://thinkpython2.com
#
# Write a function called cumsum that takes a list of numbers and 
# returns the cumulative sum; that is, a new list where the ith 
# element is the sum of the first i+1 elements from the original list.

def cumsum(li):
    total = 0 
    new_li = []
    for elem in li:
        total += elem 
        new_li.append(total)
    return new_li 

t = [1, 2, 3]
print(cumsum(t))
