import turtle

def five():
    my_pen = turtle.Turtle()
    for i in range(3):
        my_pen.forward(50)
        my_pen.right(144)
        my_pen.forward(50)
        my_pen.right(144)
    turtle.done

def six():
    my_pen = turtle.Turtle()
    for i in range(3):
        my_pen.forward(60)
        my_pen.right(60)
        my_pen.forward(60)
        my_pen.right(60)
    turtle.done()

def seven():
    a = turtle.Turtle()
    for i in range(100):
        a.dot()
        a.forward(2 + i / 4)
        a.penup()
        a.left(30 - i / 4)
    turtle.done()

five()
#  six()
#  seven()
