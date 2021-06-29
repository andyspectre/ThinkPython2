def more_anagrams(s):
    li = []
    for line in s:
        word = line.strip()
        li.append(word)
    li.sort()

    d = dict()
    for word in li:
        keyes = [len(word)]
        for key in keyes:
            if key not in d:
                d[key] = [word]
            else:
                d[len(word)].append(word)
    return d

fin = open("wordliswordlist.txt")
print(more_anagrams(fin))
