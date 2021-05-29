# Andrea Cocco 2020
# Chapter 12 Exercise 1 from the book:
#     
# Think Python, 2nd Edition
# by Allen Downey
# http://thinkpython2.com
#
# Write a function called most_frequent that takes a string and prints the 
# letters in decreasing order of frequency. Find text samples from several 
# different languages and see how letter frequency varies between languages.

from operator import itemgetter

def myli(s):
    """Take a string s, call most_frequent(s) to create a dictionary
    and then put the values in an ordered list of tuples.
    """
    words = most_frequent(s)

    li = []
    for letter, freq in words.items():
        li.append((freq, letter))

    return sorted(li, key=itemgetter(0), reverse=True) 

def most_frequent(s):
    """Take a string s and return a dictionary in which the
    key-value pairs are letter-number where letter is every
    letter in the string and number is how many times that letter
    appears.
    """
    d = dict()
    for letter in s:
        d[letter] = d.get(letter,0) + 1
    return d
    
s0 = """In informatica, una struttura dati è un'entità  usata per organizzare 
un insieme di dati all'interno della memoria del computer, ed eventualmente 
per memorizzarli in una memoria di massa"""

s1 = """In computer science, a data structure is a data organization, 
management, and storage format that enables efficient access and modification"""

s2 = """In der Informatik und Softwaretechnik ist eine Datenstruktur ein Objekt, 
welches zur Speicherung und Organisation von Daten dient."""

s3 = """En ciencias de la computaciÃ³n, una estructura de datos es una forma
particular de organizar datos en una computadora para que puedan ser 
utilizados de manera eficiente.""" 

s4 = """Een datastructuur is in de informatica een manier waarop de elementen 
(in dit verband ook wel componenten, delen of items genoemd) van een 
samengestelde variabele samenhangen."""

print("Italian:")
frequency = (myli(s0))
for n in frequency:
    print(n)

print()
print()

print("English:")
frequency = (myli(s1))
for n in frequency:
    print(n)

print()
print()

print("German:")
frequency = (myli(s2))
for n in frequency:
    print(n)

print()
print()

print("Spanish:")
frequency = (myli(s3))
for n in frequency:
    print(n)

print()
print()

print("Dutch:")
frequency = (myli(s4))
for n in frequency:
    print(n)
