#   a113_tower.py
#   Modify this code in VS Code to alternate the colors of the 
#   floors every three floors
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)
building = 4
# starting location of the tower
x = -150
y = -150

# height of tower and a counter for each floor
num_floors = 21
floor = 0

# iterate
while floor < num_floors:
  # set placement and color of turtle
  painter.penup()
  painter.goto(x, y)
  rem = floor % 6
  painter.color("gray")
  y = y + 5 # location of next floor
  floor = floor + 1

  if (rem > 2):  
    painter.color("blue")
  if (rem > 3):  
    painter.color("yellow")
  if floor == num_floors:
      floor = 0
      x = x + 70
      y = -150 
      building = building - 1
      if building < 1:
          floor = 200
          
    
      

  #draw the floor
  painter.pendown()
  painter.forward(50)
  


wn = trtl.Screen()
wn.mainloop()