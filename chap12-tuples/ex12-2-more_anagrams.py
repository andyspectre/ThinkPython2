def anagram(s):
    li = []
    for line in s:
        word = line.strip()
        li.append(word)
    li.sort()

    d = dict()
    for word in li:
        if word not in d:
            d[word] = len(word) 

    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

fin = open('wordlist.txt')
print(anagram(fin))
