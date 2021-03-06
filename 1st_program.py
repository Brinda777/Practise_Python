import turtle

turtle.bgcolor('black')
turtle.title('The National Flag of Nepal')
t = turtle.Turtle()
t.speed(4)

#BORDER

t.color('blue')  
t.penup()
t.goto(-160,-210)
t.pendown()
t.begin_fill()
t.left(90)
t.forward(428.1)
t.right(122)
t.forward(406)
t.right(148)
t.forward(222)
t.left(135)
t.forward(300)
t.right(135)
t.forward(334.1)
t.end_fill()

#VITRA KO RED

t.color('red')
t.penup()
t.goto(-150,-200)
t.pendown()
t.begin_fill()
t.right(90)
t.forward(400)
t.right(122)
t.forward(354)
t.right(148)
t.forward(212.1)
t.left(135)
t.forward(300)
t.right(135)
t.forward(300)
t.end_fill()

#SURYA

t.penup()
t.goto(-115,-115)
t.pendown()
t.color('white')
t.begin_fill()
for i in range(12):
    t.right(30)
    t.forward(22)
    t.right(120)
    t.forward(22)
    t.left(120)
t.end_fill()

#CHANDRA

t.penup()
t.goto(-115,85)
t.forward(20)
t.pendown()
t.begin_fill()
t.left(90)
t.circle(60,180)
t.left(160)
t.circle(-64,140)
t.end_fill()
t.penup()
t.goto(-103,48)
t.left(65)
t.pendown()
t.begin_fill()
for i in range(13):
    t.right(20)
    t.forward(9)
    t.right(110)
    t.forward(9)
    t.left(110)
t.end_fill()

t.hideturtle()
turtle.done()
