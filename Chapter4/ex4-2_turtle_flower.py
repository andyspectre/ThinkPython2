"""Andrea Cocco 2020
Chapter 4 Exercise 2 from the book:

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""

import turtle
import math

def polyline(turtle, nsides, sideslenght, angle):
    """Draws an n-sided polygon.
    turtle: turtle
    nsides: number of sides
    sideslenght: lengh of each side
    angle: size of angles in degrees
    """
    for i in range(nsides):
        turtle.fd(sideslenght)
        turtle.lt(angle)

def arc(turtle, r, angle):
    """Draw an arc of radius r
    r = radius of the arc
    angle = angle subtended by the arc
    """
    arc = 2 * math.pi  * r * angle / 360
    nsegments = int(arc / 3) + 1 
    segmentslenght = arc / nsegments
    outerangle = float(angle) / nsegments
    polyline(turtle, nsegments, segmentslenght, outerangle)

def petal(t, r, angle):
    """Draws a petal using two arcs.
    t: Turtle
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)

def flower(t, n, r, angle):
    """Draws a flower with n petals.
    t: Turtle
    n: number of petals
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0/n)

def move(t, length):
    """Move Turtle (t) forward (length) units without leaving a trail.
    Leaves the pen down.
    """
    t.pu()
    t.fd(length)
    t.pd()

bob = turtle.Turtle()

# draw a sequence of three flowers, as shown in the book.
move(bob, -100)
flower(bob, 7, 60.0, 60.0)

move(bob, 100)
flower(bob, 10, 40.0, 80.0)

move(bob, 100)
flower(bob, 20, 140.0, 20.0)

bob.hideturtle()
turtle.mainloop()
