import turtle


def draw_koch_curve(t, length, order):
    if order == 0:     # The base case is just a straight line
        t.fd(length)
    else:
        for angle in [60, -120, 60, 0]:
            draw_koch_curve(t, order-1, length/3)   # Go 1/3 of the way
            t.lt(angle)


def draw_snowflake(t, length, order):
    for i in range(3):
        draw_koch_curve(t, length, order)
        t.rt(120)


def draw_koch_snowflake(t, length):
    if length < 3:
        t.fd(length)
        return


bob = turtle.Turtle()
bob.pu()
bob.goto(-250, 90)
bob.pd()
print(draw_koch_curve(bob, 50, 4))
turtle.mainloop()
