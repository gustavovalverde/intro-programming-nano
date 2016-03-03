import turtle


def canvas():
    window = turtle.Screen()
    window.bgcolor("grey")


def draw_square():
    gus = turtle.Turtle()

    # customizing gus
    gus.shape("turtle")
    gus.color("blue")
    gus.speed(1)

    pos = 0
    while pos < 4:
        gus.forward(100)
        gus.right(90)
        pos += 1


def draw_circle():
    # adding a new friend
    ros = turtle.Turtle()
    ros.shape("classic")
    ros.color("pink")
    ros.speed(3)

    ros.circle(100)


canvas()
draw_square()
draw_circle()
turtle.Screen().exitonclick()
