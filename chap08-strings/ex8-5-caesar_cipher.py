import string 

def rotate_s(s, n):
    """Generate a new string out of an original string by
    shifting each letter in the string n positions down the alphabet
    s = original string
    n = number of the position for the shift
    """
    n_str = ''

    for letter in s:
        if letter.islower(): 
            start = ord('a')
        elif letter.isupper():
            start = ord('A')
        position = ord(letter) - start
        shift = (position + n) % 26 + start
        n_str += chr(shift)
    return n_str

low = string.ascii_lowercase
upper = string.ascii_uppercase
print(rotate_s('IBM', -1)) 
print(rotate_s('PNG', 13))
print(rotate_s('SHA', 13))
print(rotate_s('bin', 13))
print(rotate_s('Ares', 13))
print(rotate_s('TerrA', 13))
print(rotate_s(low, 23))
print(rotate_s(upper, 13))
