#   a114_guess.py
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.penup()
painter.color("salmon")
painter.pensize(2)

spiral_space = 140

while (spiral_space > 10): 
  painter.goto(00,0)
  painter.right(10)
  painter.forward(10+(spiral_space*2))
  painter.pendown()
  painter.circle(1)
  painter.penup()
  spiral_space = spiral_space - 1
  if (spiral_space % 5 == 0):
    painter.color("navy")
  if (spiral_space % 10 == 0):
    painter.color("salmon")

wn = trtl.Screen()
wn.mainloop()