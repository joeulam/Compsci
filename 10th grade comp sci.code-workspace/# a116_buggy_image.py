#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
x = trtl.Turtle()
x.pensize(40)   #choosing spider body pen thickness
x.circle(20) #Making spider body
lines = 6
length = 70
spacing = 380 / lines #config for legs 
x.pensize(5)
counter = 0
while (counter < lines): #while loop to draw the legs 
  x.goto(0,0)
  x.setheading(spacing*counter)
  x.forward(length)
  counter = counter + 1
x.hideturtle()
wn = trtl.Screen()
wn.mainloop()