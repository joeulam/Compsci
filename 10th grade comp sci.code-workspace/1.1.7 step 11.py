#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic","arrow", "turtle", "circle", "square", "triangle", "classic","arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold","red", "blue", "green", "orange", "purple", "gold","red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t.penup()
  t.color(turtle_colors.pop())
  t.pencolor("black")
  my_turtles.append(t)

#  The starting location for the code to run
startx = 0
starty = 0
startDir = 90 
forwardLength = 50
# The turns for each 
for t in my_turtles:
  t.goto(startx, starty)
  t.pendown()
  t.setheading(startDir)
  t.right(45)     
  t.forward(forwardLength)

#	Increments to allow the lines to keep moving upwards to show all the shapes 
  startx = t.xcor()
  starty = t.ycor()
  startDir = t.heading()
  forwardLength += 3

wn = trtl.Screen()
wn.mainloop()