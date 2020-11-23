#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
x = trtl.Turtle()
x.pensize(40)   #choosing spider body pen thickness
x.circle(20) #Making spider body

x.goto(0,-25)
x.pensize(10)
x.circle(10)

lines = 8
length = 70
spacing = 240 / lines #config for legs 
x.pensize(5)


counter = 0
while (counter < lines/2): #while loop to draw the legs 
  x.penup()
  x.goto(0,20)
  x.pendown()
  x.setheading(spacing*counter-60+240)
  x.circle(50,-120)
  counter = counter + 1

counter = 0
while (counter < lines/2): #while loop to draw the legs 
  x.penup()
  x.goto(0,20)
  x.pendown()
  x.setheading(spacing*counter-45+150)
  x.circle(50,120)
  counter = counter + 1

x.pencolor("white")
x.fillcolor("white")
x.penup()
x.goto(-10,-25)
x.begin_fill()
x.pendown()
x.circle(3)
x.end_fill()
x.penup()
x.goto(10,-25)
x.begin_fill()
x.pendown()
x.circle(3)
x.end_fill()

x.hideturtle()
wn = trtl.Screen()
wn.mainloop()