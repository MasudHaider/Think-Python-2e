import turtle
import math


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polygon(t, length, n):
    angle = 360.0 / n
    polyline(t, length, n, angle)


def polyline(t, length, n, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def circle(t, r):
    arc(t, r, 78)


def arc(t, r, angle):
    circumference = 2 * math.pi * r
    length = circumference * (angle / 360)
    n = int(length / 3) + 1
    step_length = length / n
    step_angle = float(angle) / n
    polyline(t, step_length, n, step_angle)


bob = turtle.Turtle()
print(circle(bob, 67))
turtle.mainloop()

