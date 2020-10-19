import turtle as trtl

painter = trtl.Turtle()
painter.speed(99999)

# stem
painter.color("green")
painter.pensize(15)
painter.goto(0, -150)
painter.setheading(90)
painter.forward(100)
#  leaf
painter.setheading(270)
painter.circle(20, 120, 20)
painter.setheading(90)
painter.goto(0, -60)
# rest of stem
painter.forward(60)
painter.setheading(0)

# change pen
painter.penup()
painter.shape("circle")
painter.turtlesize(3)

# draw flower
painter.color("darkorchid")
painter.goto(20,180)
petals = 0
while (petals < 9):
  painter.right(40)
  painter.forward(60)
  painter.stamp()
  petals = petals + 1

painter.goto(20,160)
painter.color("blue")
petals = 0
while (petals < 12):
  painter.right(30)
  painter.forward(30)
  painter.stamp()
  petals = petals + 1


painter.goto(20,120)
painter.color("green")
while petals < 100:
    painter.right(5)
    painter.forward(1)
    painter.stamp()
    petals = petals + 1

wn = trtl.Screen()