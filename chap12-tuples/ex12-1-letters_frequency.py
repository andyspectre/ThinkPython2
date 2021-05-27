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
    words = most_frequent(s)

    li = []
    for letter, freq in words.items():
        li.append((freq, letter))

    return sorted(li, key=itemgetter(0), reverse=True) 

def most_frequent(s):
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

frequency = (myli(s0))
for n in frequency:
    print(n)

print()
print()

frequency = (myli(s1))
for n in frequency:
    print(n)

print()
print()

frequency = (myli(s2))
for n in frequency:
    print(n)

print()
print()

frequency = (myli(s3))
for n in frequency:
    print(n)
