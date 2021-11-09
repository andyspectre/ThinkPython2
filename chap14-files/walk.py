# Andrea Cocco 2021
# Chapter 14 Exercise p.168 from the book:
#     
# Think Python, 2nd Edition
# by Allen Downey
# http://thinkpython2.com

"""The os module provides a function called walk that is similar to this 
one but more versatile. As an exercise, read the documentation and use it 
to print the names of the files in a given directory and its subdirectories.
"""

import os
for root,dirs,files in os.walk('c:/users/andre/git'):
    print()
    print(root)
    files = (f for f in files if not f[0]=='.')
    dirs[:] = (d for d in dirs if not d[0]=='.')
    for name in files:
        print(os.path.join(root,name))
