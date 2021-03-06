import turtle


def draws():
    window = turtle.Screen()
    window.bgcolor("grey")
    draw_flower()
    window.exitonclick()


def draw_flower():
    flower = turtle.Turtle()
    flower.shape("turtle")
    flower.color("blue")
    flower.speed(10)

    for degrees in range(0, 40):
        for sides in range(0, 4):
            flower.forward(100)
            flower.left(90)
        flower.left(10)


def draw_square():
    box = turtle.Turtle()
    box.shape("turtle")
    box.color("blue")
    box.speed(1)

    sides = 0
    while sides < 4:
        box.forward(100)
        box.right(90)
        sides += 1


def draw_circle():
    donna = turtle.Turtle()
    donna.shape("classic")
    donna.color("pink")
    donna.speed(3)

    donna.circle(100)


def draw_triangle():
    egypt = turtle.Turtle()
    egypt.shape("turtle")
    egypt.color("orange")
    egypt.speed(1)

    sides = 0
    while sides < 3:
        egypt.forward(-100)
        egypt.left(120)
        sides += 1

draws()
