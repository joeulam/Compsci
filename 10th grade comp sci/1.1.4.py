#   a114_zero_iteration_and_infinite.py
#   Make a zero-iteration condition and follow it with an infinite loop.
#   Include some visual evidence that the second loop is infinite.
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(10)
time = 0
# Add a loop with a zero-iteration condition
while (time <= 10):
  painter.forward(20)
  painter.right(10)
  painter.stamp()
  painter.circle(10)
  time = time + 1 
# Add an infinite loop
while (time >= 10):
  painter.forward(20)
  painter.right(10)
  painter.stamp()
  painter.circle(10)
  time = time + 1 


wn = trtl.Screen()
wn.mainloop()