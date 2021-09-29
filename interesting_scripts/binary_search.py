""" Implement binary search: takes a list and a value as arguments,
returns the index of the value in the list
"""
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
    raise LookupError

l = ["Italia", "Vaticano", "San Marino", "Francia", "Svizzera", "Austria", "Slovenia"] 
l.sort()
print(binary_search(l, "Francia"))
