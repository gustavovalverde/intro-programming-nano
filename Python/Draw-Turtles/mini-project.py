import turtle


def draw_flower():
    window = turtle.Screen()
    window.bgcolor("white")

    rose = pencil(2, "arrow", "red", 5)
    pikachu = pencil(2, "arrow", "yellow", 5)
    hulk = pencil(2, "arrow", "green", 5)

    hulk.begin_fill()
    hulk.down()
    draw_stem(hulk, 50, 8)
    hulk.up()
    hulk.end_fill()

    rose.begin_fill()
    rose.down()
    num_petals = 8
    for petal in xrange(num_petals):
        rose.setheading(0)
        rose.right(360 * petal/num_petals)
        draw_petal(rose, 75, 8)
    rose.up()
    rose.end_fill()

    draw_center(pikachu)

    window.exitonclick()


def pencil(penSize, penShape, penColor, penSpeed):
    myPen = turtle.Turtle()
    myPen.hideturtle()
    myPen.pensize(penSize)
    myPen.shape(penShape)
    myPen.color(penColor)
    myPen.speed(penSpeed)
    return myPen


def draw_petal(myPen, radius, steps):
    myPen.circle(radius, 90, steps)
    myPen.left(90)
    myPen.circle(radius, 90, steps)


def draw_center(myPen):
    myPen.dot(30)


def draw_stem(myPen, radius, steps):
    myPen.right(90)
    myPen.forward(175)
    myPen.setheading(0)
    draw_petal(myPen, radius, steps)
    myPen.setheading(90)
    draw_petal(myPen, radius, steps)
    myPen.right(90)
    myPen.forward(75)

draw_flower()
