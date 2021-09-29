""" Open a file and create a list. Check if a word is in that list. """
def create_list(f):
    myli = []
    for lines in f:
        word = lines.strip()
        myli.append(word)
    myli.sort()
    return myli

fin = open("pass_list.txt")
popular_passwords = create_list(fin)
your_password = "password"

if your_password in popular_passwords:
    print(your_password, "is in the list")
else:
    print(your_password, "is not in the list")

