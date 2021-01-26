import turtle as trtl
import random as rand
#### maze configuration variables
num_walls = 25
path_width = 15
wall_color = 'black'


#### config maze
maze_painter = trtl.Turtle()
maze_painter.pensize(4)
maze_painter.pencolor(wall_color)
maze_painter.speed(0)

#### config runner
maze_runner = trtl.Turtle()
maze_runner.penup()

#### Functions
def draw_door(dist):
  maze_painter.forward(dist)
  if (rand.randint(0,2) != 2): #[0,1,2]
    maze_painter.penup()
  maze_painter.forward(path_width * 3)
  maze_painter.pendown()

def draw_barrier(dist):
  maze_painter.forward(dist)
  if (rand.randint(0,3) != 1): #[0,1,2,3]
    maze_painter.left(90)
    maze_painter.forward(path_width * 2)
    maze_painter.backward(path_width * 2)
    maze_painter.right(90)

### Event Handlers
def up_key():
  maze_runner.setheading(90)

def down_key():
  maze_runner.setheading(270)

def left_key():
  maze_runner.setheading(180)

def right_key():
  maze_runner.setheading(0)


#### draw maze from the middle out
wall_len = path_width
for wall in range(num_walls):
  #[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

  maze_painter.left(90)
  wall_len += path_width
  if (wall >= 4):
    # randomize location of doors and barriers in wall
    door = rand.randint(path_width*2,wall_len-path_width*2)
    barrier = rand.randint(path_width*2,wall_len-path_width*2)
    # if door and barrier would be rendered on top of each other, get new location for both
    while abs(door - barrier) < path_width:
      door = rand.randint(path_width*2,wall_len-path_width*2)
      barrier = rand.randint(path_width*2,wall_len-path_width*2)
  
    if (door < barrier):
      # draw door first
      draw_door(door)
      # draw barrier, subtract door lengths
      draw_barrier(barrier - door - path_width*2)
      # draw remaining wall, subtracting barrier length
      maze_painter.forward(wall_len - barrier)

    else:
      # draw barrier first
      draw_barrier(barrier)
      # draw wall, subtract barrier length
      draw_door(door - barrier)
      #draw remaining wall, subtracting door lengths
      maze_painter.forward(wall_len - door - path_width*2)

maze_painter.hideturtle()
def move_runner():
  maze_runner.forward(1)
#determine if runner hits the wall
  wn_canvas = wn.getcanvas()
  x, y = maze_runner.position()
  margin = 10
  items = wn_canvas.find_overlapping(x+margin, -y+margin, x-margin, -y-margin)

  # check if canvas is not empty
  if (len(items) > 0):
    canvas_color = wn_canvas.itemcget(items[0], 'fill')
    if (canvas_color) == wall_color:
      # stop game 
      maze_runner.fillcolor('grey')
      wn.onkeypress(None, 'g')
      return


maze_runner.goto(-40,30)
maze_runner.shape("turtle")
maze_runner.color("blue")
wn = trtl.Screen()
wn.onkeypress(up_key,"Up")
wn.onkeypress(up_key, 'w')
wn.onkeypress(down_key,"Down")
wn.onkeypress(down_key, 's')
wn.onkeypress(left_key,"Left")
wn.onkeypress(left_key, 'a')
wn.onkeypress(right_key,"Right")
wn.onkeypress(right_key, 'd')
wn.onkeypress(move_runner, 'g')

wn.listen()
wn.mainloop()