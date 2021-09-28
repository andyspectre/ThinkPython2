def find(word, letter, index):
    if not isinstance(index, int):
        raise TypeError
    if index > len(word):
        raise IndexError
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    raise IndexError("Letter not found in the word") 

w = "home"
l = 'w'
i = 0
print(find(w, l, i))
