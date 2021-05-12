# Andrea Cocco 2020
# Chapter 10 Exercise 1 from the book:
#     
# Think Python, 2nd Edition
# by Allen Downey
# http://thinkpython2.com
#
# Write a function called nested_sum that takes a list of lists 
# of integers and adds up the elements from all of the nested lists.

def nested_sum(li):
    """Compute the sum of all numbers in a nested list of integers.
    li = nested list of integers
    """
    total = 0
    for nested in li:
        total += sum(nested)
    return total

li = [[1, 2], [3], [4, 5, 6]]
print(nested_sum(li))
