import turtle as trtl 
import random as rand

start_game = False
answer = input("Are you ready to start? yes or no ")

if answer == "yes":
  spot_color = 'pink'
  spot_size = 2 
  spot_shape = 'circle'
  score = 0
  font_setup = ('Arial',20,'normal')
  counter =  trtl.Turtle()
  font_setup = ("Arial", 20, "normal")
  timer = 30
  counter.penup()
  counter.goto(150,150)
  counter.pendown()
  counter.hideturtle()
  counter_interval = 1000   #1000 represents 1 second
  timer_up = False
  colors = ["orange","red","black","blue","yellow","white"]

  size = [.5,1,2,3,4,5,6,7,8,9]

  spot = trtl.Turtle()
  spot.shape(spot_shape)
  spot.shapesize(spot_size)
  spot.fillcolor(spot_color)

  Score_writer = trtl.Turtle()
  Score_writer.penup()
  Score_writer.hideturtle()
  Score_writer.goto(-180,140)

  def spot_clicked(x,y):
    spot_color = rand.choice(colors)
    spot.fillcolor(spot_color)
    spot.stamp()
    spot_color = "pink"
    spot.fillcolor(spot_color)
    spot_size = rand.choice(size)
    spot.shapesize(spot_size)
    change_postition()
    update_score()
    print("clicked")
    


  def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
      counter.write("Time's Up", font=font_setup)
      timer_up = True
    else:
      counter.write("Timer: " + str(timer), font=font_setup)
      timer -= 1
      counter.getscreen().ontimer(countdown, counter_interval) 


  def change_postition():
    new_xpos = rand.randint(-200,200)
    new_ypos = rand.randint(-150,150)
    spot.penup()
    spot.hideturtle()
    spot.goto(new_xpos , new_ypos)
    spot.showturtle()
    spot.pendown()

  def update_score():
    global score 
    score += 1
    Score_writer.clear()
    Score_writer.write(score, font=font_setup)

  spot.onclick(spot_clicked)
elif "no":
  print("Canceling")
else:
  print("Error")

wn = trtl.Screen()
wn.bgcolor("green")
wn.ontimer(countdown, counter_interval) 
wn.mainloop()