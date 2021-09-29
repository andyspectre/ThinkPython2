"""Generate a new string out of an original string by
shifting each letter in the string n positions down the alphabet
s = original string
n = number of the position for the shift
"""
def rotate_s(s, n):
    n_str = ""

    for letter in s:
        if letter.islower(): 
            start = ord('a')
        elif letter.isupper():
            start = ord('A')
        position = ord(letter) - start
        shift = (position + n) % 26 + start
        n_str += chr(shift)
    return n_str

li = list(range(1, 25))

for i in li:
    print(rotate_s("andrea", i))
