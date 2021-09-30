""" Find if a word is a palindrome """
def is_palindrome(w):
    return w == w[::-1]

print(is_palindrome("radar"))
print(is_palindrome("Italia"))

