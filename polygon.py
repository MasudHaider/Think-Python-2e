import turtle
import math

print("__main__ : bob = Turtle()")
print("circle : t = bob(Turtle object), r = 67")
print("arc : t = bob(Turtle object), r = 67, angle = 360", end="")
print("circumference = 2*pi*r = 420.97, length = 420.97, n = 141, step_length=2.98, step_angle=2.55")
print("polyline : t = bob(Turtle object), length = 2.98, n=141, angle=2.55")


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
    arc(t, r, 360)


def arc(t, r, angle):
    circumference = 2 * math.pi * r
    length = circumference * (angle / 360)
    n = int(length / 4) + 3
    step_length = length / n
    step_angle = float(angle) / n
    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, step_length, n, step_angle)
    t.rt(step_angle/2)


# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__ == '__main__':
    bob = turtle.Turtle()

    # draw a circle centered on the origin
    # radius = 100
    # bob.pu()
    # bob.fd(radius)
    # bob.lt(90)
    # bob.pd()
    print(arc(bob, 100, 80))

    # wait for the user to close the window
    turtle.mainloop()