import turtle as trtl

painter = trtl.Turtle()
painter.pensize(5)

# draw curved arc
painter.penup()
painter.goto(0, -20)
painter.pendown()
painter.circle(100, 180)

# draw segmented arc 
painter.penup()
painter.goto(0, 20)
painter.pendown()
painter.circle(100, 180, 3)

wn = trtl.Screen()
wn.mainloop()