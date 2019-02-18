import turtle
from polygon import arc


def draw_petal(t, r, angle):
    for k in range(2):
        arc(t, r, angle)
        t.lt(180-angle)


def draw_flower(t, r, angle, petals):
    for k in range(petals):
        draw_petal(t, r, angle)
        t.lt(360.0/petals)


def move_turtle(t, length):
    # Move the turtle forward (length) units without leaving trail
    t.pu()
    t.fd(length)
    t.pd()


bob = turtle.Turtle()
move_turtle(bob, -100)
print(draw_flower(bob, 60.0, 60.0, 7))
move_turtle(bob, 100)
print(draw_flower(bob, 40.0, 80.0, 10))
move_turtle(bob, 100)
print(draw_flower(bob, 140.0, 20.0, 20))
bob.hideturtle()
turtle.mainloop()
