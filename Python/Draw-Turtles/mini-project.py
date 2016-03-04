import turtle


def draw_flower():
    window = turtle.Screen()
    window.bgcolor("white")

    rose = pencil(2, "arrow", "red", 2)
    pikachu = pencil(2, "arrow", "yellow", 2)
    hulk = pencil(2, "arrow", "green", 2)

    draw_center(pikachu)
    draw_petal(rose)

    window.exitonclick()


def pencil(penSize, penShape, penColor, penSpeed):
    myPen = turtle.Turtle()
    myPen.hideturtle()
    myPen.pensize(penSize)
    myPen.shape(penShape)
    myPen.color(penColor)
    myPen.speed(penSpeed)
    return myPen

num_petals = 8

def draw_petal(myPen, num_petals, radius, steps):
    myPen.circle(radius, 90, steps)
    myPen.left(90)
    myPen.circle(radius, 90, steps)
    steps = 8
radius = 100

for petal in xrange(num_petals):
    myPen.setheading(0)
    myPen.right(360 * petal/num_petals)
    draw_petal(radius, steps)





def draw_center(myPen):
    myPen.dot(30)

draw_flower()
