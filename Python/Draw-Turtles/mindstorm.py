import turtle


def draw_square():
    window = turtle.Screen()
    window.bgcolor("grey")

    gus = turtle.Turtle()

    # customizing gus
    gus.shape("turtle")
    gus.color("blue")
    gus.speed(1)

    gus.forward(100)
    gus.right(90)
    gus.forward(100)
    gus.right(90)
    gus.forward(100)
    gus.right(90)
    gus.forward(100)
    gus.right(90)

    # adding a new friend
    ros = turtle.Turtle()
    ros.shape("classic")
    ros.color("pink")
    ros.speed(3)

    ros.circle(100)

    window.exitonclick()

draw_square()
