import turtle as trtl
import random as rand
#### maze configuration variables
num_walls = 25
path_width = 15
wall_color = "black"


#### config maze
maze_painter = trtl.Turtle()
maze_painter.pensize(4)
maze_painter.pencolor(wall_color)
maze_painter.speed(0) #fastest speed


#### draw maze from the middle out
wall_len = path_width
for wall in range(num_walls):
  maze_painter.left(90)
  wall_len += path_width

  if (wall >= 4):
    #randomize location of door and barriers in wall
    door = rand.randint(path_width * 2, (wall_len-(2*path_width)))
    barrier = rand.randint(path_width*2, (wall_len-2*path_width))
    #if door and barrier would be rendered on top of each other, get a new value for both
    while (abs(door - barrier) < path_width):
      door = rand.randint(path_width * 2, (wall_len-(2*path_width)))
      barrier = rand.randint(path_width*2, (wall_len-2*path_width))

    if (barrier < door):
      #draw barrier first
      maze_painter.forward(barrier)
      maze_painter.left(90)
      maze_painter.forward(path_width*2)
      maze_painter.backward(path_width*2)
      maze_painter.right(90)

      #draw door, subtract barrier lengths already drawn
      maze_painter.forward(door - barrier)
      maze_painter.penup()
      maze_painter.forward(2*path_width)
      maze_painter.pendown()

      #draw remaining wall, subtracting door length
      maze_painter.forward(wall_len - (door + path_width*2))
      
    else:
      #draw door first
      maze_painter.forward(door)
      maze_painter.penup()
      maze_painter.forward(path_width*2)
      maze_painter.pendown()

      #draw barrier, subtract door lengths already drawn
      maze_painter.forward(barrier - (door + path_width*2))
      maze_painter.left(90)
      maze_painter.forward(path_width*2)
      maze_painter.backward(path_width*2)
      maze_painter.right(90)

      #draw remaining wall, subtracting barrier lengths already drawn
      maze_painter.forward(wall_len - barrier)

'''
place the turtle in the middle of the screen
iterate until 25 sides are drawn
  turn left
  increase length of wall

  create door, barrier variables
  get random length to door
  get random length to barrier
  if door/barrier are in the same location
    get new location
  if barrier is first:
    draw part of wall to barrier
    turn left
    draw barrier to inner wall
    go back to original wall
    turn right

    # draw door
    draw part of wall from barrier to door
    turtle = pen up
    "draw" door width
    turtle = pen down 

    draw remaining wall

  else:
    #draw door
    draw part of wall to door
    turtle = pen up
    "draw" door width
    turtle = pen down

    # draw barrier
    draw part of wall from door to barrier
    turn left
    draw barrier to inner wall
    go back to original wall
    turn right
    draw remaining wall
'''
maze_painter.hideturtle()

wn = trtl.Screen()
wn.mainloop()