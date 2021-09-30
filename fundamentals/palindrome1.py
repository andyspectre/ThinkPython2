"""Check if a word is a palindrome"""
def is_palindrome(myword):
    # If the lenght of a word is only one character, it is a palindrome
    if len(myword) <= 1:
        return True
    # If first and last letter are different, it is NOT a palindrome
    if  myword[0] != myword[-1]:
        return False
    # Call again this function, this time excluding first and last letter
    return is_palindrome(myword[1:-1])

print(is_palindrome("radar"))
