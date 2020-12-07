#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl
import random
# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle"] #"classic"]#turtle shape
horiz_colors = ["red", "blue", "green", "orange", "purple"] #"gold"]#color for horizontal objects
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo"] #"brown"]#color for vertical object 

tloc = 50
for s in turtle_shapes:

  ht = trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-350, tloc)
  ht.setheading(0)

  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 350) #tloc is x corrinate but opposite 
  vt.setheading(270) # where it is heading 
  
  tloc += 50

hit = False
steps = 0
while len(horiz_turtles) > 0:
  for t in horiz_turtles:
    n = random.randint(1,22)
    print(n)
    t.forward(n)
    if t.xcor() > -10:
      t.right(180)
    elif t.xcor() < -390:
      t.left(180)
  for t in vert_turtles:
    t.forward(n + 2)
    if t.ycor() < 10:
      t.right(180)
      
    elif t.ycor() >390:
      t.left(180)


  for h in horiz_turtles:
    for v in vert_turtles:
      xDistance = abs(h.xcor()-v.xcor())
      yDistance = abs(h.ycor()-v.ycor())
      if xDistance <10: #collision of the two turtles
        if yDistance < 10:
          #horiz_turtles.remove(h) 
          #vert_turtles.remove(v)
          hit = True
          h.right(180)
          v.right(180)


  
  
    

  steps = steps + 1
          
# TODO: move turtles across and down screen, stopping for collisions
"""
steps = 0
while steps < 50:
	steps = steps + 1
"""

wn = trtl.Screen()
wn.mainloop()
