"""Andrea Cocco 2020
Chapter 4 Exercise 3 from the book:
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""

import turtle
import math

def isosceles(t, r, angle):
    """Draw isosceles triangles:
    t: turtle
    r: size of triangle sides
    angle: angle in degrees
    """

    y = r*math.sin(math.radians(angle))
    t.rt(angle)
    t.fd(r)
    t.lt(90+angle)
    t.fd(2*y)
    t.lt(90+angle)
    t.fd(r)
    t.lt(180-angle)

def polypie(t, n, r):
    """defines a regular polygon of n sides of lenght r
    n: number of sides
    r: lenght of sides
    """
    angle = 360.0 / n #external angles of a regular polygon
    for i in range(n):
        isosceles(t, r, angle/2)
        t.lt(angle)

def draw_pie(t, n, r):
    """Draw a regular polygon of n sides of lenght r:
    t: turtle
    n: number of sides
    r: lenght of sides
    """
    polypie(t, n, r)
    t.pu()
    t.fd(r*2+10)
    t.pd()

bob = turtle.Turtle()
bob.speed(8)
bob.pu()
bob.bk(130)
bob.pd()
size = 40

draw_pie(bob, 1, size)
draw_pie(bob, 2, size)
draw_pie(bob, 3, size)
draw_pie(bob, 5, size)
draw_pie(bob, 6, size)
draw_pie(bob, 7, size)
draw_pie(bob, 8, size)

turtle.mainloop()
