#   a115_robot_maze.py
import turtle as trtl

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

#------ robot commands
def move():
  robot.dot(10)
  robot.fd(50)

def turn_left():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)

#----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "robot.gif"
wn.addshape(robot_image)

#----- init robot
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()

#---- TODO: change maze here
wn.bgpic("maze3.png") # other file names should be maze2.png, maze3.png

#---- TODO: begin robot movement here
# move robot forward with move()
# turn robot left with turn_left()
# sample while loop:
'''
i = 0
while (i < 3): # forward 3
  move()
  i = i + 1 
'''

#---- end robot movement 
p = 0
once = 0
x = 0

while once < 1:
  while x < 1:
    move()
    x = x + 1
    
  while x < 4:
    turn_left()
    x = x + 1
  while x < 5:
    move()    
    x = x + 1 
  while x < 6:
    turn_left()
    x = x + 1
  while x < 7:
    move()
    x = x + 1
    once = once + 1
  while x < 10:
    turn_left()
    x = x + 1
  while x < 11:
    move()
    x = x + 1
    robot.pencolor("red")
  x = 0
  while x < 1:
    move()
    x = x + 1
  while x < 2: 
    turn_left()
    x = x + 1 
  while x < 4:
    move()
    x = x + 1
  while x < 7: 
    turn_left()
    x = x + 1 
  while x < 8:
    move()
    x = x + 1
  
wn.mainloop()