#   a116_ladybug.py
import turtle as trtl

# create ladybug head
ladybug = trtl.Turtle()




# config dots


# draw two sets of dots


lines = 6
length = 50
spacing = 240 / lines #config for legs 
ladybug.pensize(5)

counter = 0
while (counter < lines/2): #while loop to draw the legs 
  ladybug.goto(0,-30)
  ladybug.setheading(spacing*counter-45)
  ladybug.forward(length)
  counter = counter + 1

counter = 0
while (counter < lines/2): #while loop to draw the legs 
  ladybug.goto(0,-30)
  ladybug.setheading(spacing*counter-45+180)
  ladybug.forward(length)
  counter = counter + 1

ladybug.setheading(0)
ladybug.penup()
ladybug.goto(0,0)
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(5)

# and body
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

while (num_dots <= 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)

  # position next dots
  ypos += 25
  xpos +=  5
  num_dots += 1
ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()