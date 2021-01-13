#   a123_apple_1.py
import turtle as trtl
import random as rand

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
ground_height = -150
x_offset = 10
y_offset = 25
letter_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
current_letter = 'A'
apple_letters = []
apple_list = []
number_of_apples = 5
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")
apple = trtl.Turtle()
apple.penup()
wn.tracer(False)

#-----functions-----
#TODO Create a function that takes a turtle as its parameter and gives that turtle (apple)a new location on the tree, only if the list of letters is not empty. Associate the turtle with a new letter selected at random from the list of letters
def reset_apple(active_apple):
  global current_letter
  length_of_list = len(letter_list)
  if(length_of_list != 0):
    x = rand.randint(-200,200)
    y = rand.randint(0,200)
    active_apple.goto(x,y) #Choose a random spot for the apple to appear 
    index = rand.randint(0,length_of_list-1)
    current_letter = letter_list.pop(index) #assigns an apple a letter 
    draw_apple(active_apple, current_letter) 
    apple_letters.append(current_letter)
    print(apple_letters)

#TODO Create a function that takes a turtle (apple) and its corresponding letter from the letter list and draws that letter on that turtle (apple)
def draw_letter(letter,active_apple):
  active_apple.color('white')
  remember_position= active_apple.position() 
  active_apple.setpos(active_apple.xcor()-x_offset,active_apple.ycor()-y_offset) #sets the position of where the apple is gonna be located 
  active_apple.write(letter, font=('Arial', 25,'bold'))
  active_apple.setpos(remember_position)
  active_apple.showturtle()

#TODO Create a function that takes a turtle (apple) and its corresponding letter from the letter list and set that turtle to be shaped by the image file, call the letter drawing function, and update the Screen
def draw_apple(active_apple,letter):
  active_apple.shape(apple_image)
  draw_letter(letter, active_apple)
  wn.update() #updates the game screen after an apple letter is pressed 

#TODO Iterate over the numbers from 0 to the number of apples, creating that many turtles calling your function that resets the apples by giving them a new random location add the new apples to a list of apples to be used in the rest of the program. The loop below executes the correct number of times by using the range() function to create a list of numbers to iterate over.
for i in range(0, number_of_apples): #[0,1,2,3,4]
  active_apple = trtl.Turtle(shape = apple_image)
  active_apple.penup() #number of apple that can be up at once 
  reset_apple(active_apple)
  apple_list.append(active_apple)

#TODO Create a function that takes a letter as its parameter, uses that letter to retrieve the corresponding turtle (apple) and causes both to drop from the tree simultaneously. Once the  apple and letter have dropped, call the apple resetting function.
def drop_apple(letter):
  wn.tracer(True)
  index = apple_letters.index(letter) #pairs apple and letter
  apple_letters.pop(index)
  active_apple = apple_list.pop(index)
  active_apple.goto(apple.xcor(), ground_height) #postioning of apple 
  active_apple.clear()
  active_apple.hideturtle() #hides turtle after dropping it
  wn.tracer(False)
  reset_apple(active_apple)
  apple_list.append(active_apple)

#TODO define a function per letter that you will use in your program. Each function should check to see if the given letter is in the list of letters; if it is, it should drop the corresponding apple.
def check_apple_a(): #checks the imput and see if they match with keystrokes 
  if('A' in apple_letters):
    drop_apple('A')
def check_apple_b():
  if('B' in apple_letters):
    drop_apple('B')
def check_apple_c ():
  if('C' in apple_letters):
    drop_apple('C')
def check_apple_d():
  if('D' in apple_letters):
    drop_apple('D')
def check_apple_e():
  if('E'in apple_letters):
    drop_apple('E')
def check_apple_f():
  if('F' in apple_letters):
    drop_apple('F')
def check_apple_g():
  if('G' in apple_letters):
    drop_apple('G')
def check_apple_h():
  if('H' in apple_letters):
    drop_apple('H')
def check_apple_i():
  if('I' in apple_letters):
    drop_apple('I')
def check_apple_j():
  if('J' in apple_letters):
    drop_apple('J')
def check_apple_k():
  if('K' in apple_letters):
    drop_apple('K')
def check_apple_l():
  if('L' in apple_letters):
    drop_apple('L')
def check_apple_m():
  if('M' in apple_letters):
    drop_apple('M')
def check_apple_n():
  if('N' in apple_letters):
    drop_apple('N')
def check_apple_o():
  if('O' in apple_letters):
    drop_apple('O')
def check_apple_p():
  if('P' in apple_letters):
    drop_apple('P')
def check_apple_q():
  if('Q' in apple_letters):
    drop_apple('Q')
def check_apple_r():
  if('R' in apple_letters):
    drop_apple('R')
def check_apple_s():
  if('S' in apple_letters):
    drop_apple('S')
def check_apple_t():
  if('T' in apple_letters):
    drop_apple('T')
def check_apple_u():
  if('U' in apple_letters):
    drop_apple('U')
def check_apple_v():
  if('V' in apple_letters):
    drop_apple('V')
def check_apple_w():
  if('W' in apple_letters):
    drop_apple('W')
def check_apple_x():
  if('X' in apple_letters):
    drop_apple('X')
def check_apple_y():
  if('Y' in apple_letters):
    drop_apple('Y')
def check_apple_z():
  if('Z' in apple_letters):
    drop_apple('Z')
#TODO use the onkeypress method of wn to correlate the functions you defined above with each of the letters that the user might type. onkeypress requires that you name one function that must take no arguments to be called when the specified key is pressed.
wn.onkeypress(check_apple_a, 'a')
wn.onkeypress(check_apple_b, 'b')
wn.onkeypress(check_apple_c, 'c')
wn.onkeypress(check_apple_d, 'd')
wn.onkeypress(check_apple_e, 'e')
wn.onkeypress(check_apple_f, 'f')
wn.onkeypress(check_apple_g, 'g')
wn.onkeypress(check_apple_h, 'h')
wn.onkeypress(check_apple_i, 'i')
wn.onkeypress(check_apple_j, 'j')
wn.onkeypress(check_apple_k, 'k')
wn.onkeypress(check_apple_l, 'l')
wn.onkeypress(check_apple_m, 'm')
wn.onkeypress(check_apple_n, 'n')
wn.onkeypress(check_apple_o, 'o')
wn.onkeypress(check_apple_p, 'p')
wn.onkeypress(check_apple_q, 'q')
wn.onkeypress(check_apple_r, 'r')
wn.onkeypress(check_apple_s, 's')
wn.onkeypress(check_apple_t, 't')
wn.onkeypress(check_apple_u, 'u')
wn.onkeypress(check_apple_v, 'v')
wn.onkeypress(check_apple_w, 'w')
wn.onkeypress(check_apple_x, 'x')
wn.onkeypress(check_apple_y, 'y')
wn.onkeypress(check_apple_z, 'z')
#-----function calls-----
wn.listen()
wn.mainloop()