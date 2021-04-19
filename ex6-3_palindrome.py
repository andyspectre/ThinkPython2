
def is_palindrome(myword):
    """Check if a word is a palindrome"""
    # If the lenght of a word is only one character, it is a palindrome
    if len(myword) <= 1:
        return True
    # If first and last word are different, it is NOT a palindrome
    if  myword[0] != myword[-1]:
        return False
    # call again this function, this time excluding first and last characters
    return is_palindrome(myword[1:-1])

def ask_word():
    """Prompt the user to enter the word to check"""
    x = input('Insert a word to check if it is a palindrome and press enter: ')
    print(is_palindrome(x))
    quit()

def quit():
    """Prompt the user to choose if he wants to quit or not"""
    quit = input('Do you want to quit? y/n ')
    if quit == 'y':
        print('Goodbye!')
    else: 
        ask_word()

ask_word()
