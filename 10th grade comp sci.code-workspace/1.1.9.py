import turtle as trtl
import random as rd
t = trtl.Turtle()
distance = 0
t.speed(0)
t.pensize(5)
t.penup()
t.goto(-100,-200)
t.pendown()
gy = input("choose a tree color: ")
t.fillcolor(gy)
t.pencolor(gy)
t.begin_fill()
x = 0
y = 0
tree = False
left = 0
heading = 45
xa = -150 #x axis
ya = 0 #y axis
t.goto(-250,-200)
p = True 
while p == True:
    while x < 20:#tree edges
        x = x + 10
        t.setheading(heading)
        t.forward(distance)
        t.goto(xa,ya)
        distance = distance - 100
        ya = ya + 150 #hights of pulling it in 
        heading = 0 #changes the tree inward drawing
        print("1")
        left = left + 1 
        if left > 1: #tip of tree
            t.setheading(180)
            t.forward(85)
            t.setheading(45)
            t.forward(235)
            
            print("runned")

    t.penup()
    t.goto(-100,-200)
    t.pendown()
    t.goto(100,-200)
    distance = 235
    xa1 = 100
    ya1 = 5
    left = 0
    
    while y < 20: #tree edges
        y = y + 10
        t.setheading(120)
        t.forward(distance)
        t.goto(xa1,ya1)
        distance = distance - 70
        ya1 = ya1 + 143
        print("1")
        left = left + 1 
        if left > 1: 
            t.setheading(135)
            t.forward(237)
            print(distance)
    t.end_fill()

    
    t.penup()
    t.goto(-20,-330)
    t.pendown()

    heading = 90
    distance = 0
    t.pencolor("brown")
    rl = 2#right side of rect
    while tree == False:
        if rl == 2: #drawing the long side of rect
            t.setheading(90)
            t.goto(-30,-350)
            t.forward(150)
            t.penup()
            t.goto(-120,-350)
            t.pendown()
            t.forward(150)
            rl = rl + 1
        else: #drawing the short side of rect
            t.setheading(0)
            t.penup()
            t.goto(-120,-350)
            t.pendown()
            t.forward(90)
            t.penup()
            t.goto(-120,-200)
            t.pendown()
            t.forward(90)
            heading = 0 
            tree = True
    pe = -118#goto's to fill in lines
    pp = -200#goto's to fill in lines 
    g = 2#varible to fill in blank line
    while g == 2: 
        t.goto(pe,pp)
        t.forward(90)
        pp = pp - 1 
        if pp < -350:
            g = g + 1
    pe = -104
    pp = -185
    t.pensize(10)
    t.pencolor(gy)
    while g == 3:
        t.penup()
        t.goto(pe,pp)
        t.pendown()
        t.setheading(86)
        t.forward(494)
        g = g + 1 

    
    snow = 0 #snowflakes 
    location = 0 
    t.pensize(5)
    
    t.pencolor("grey")#color
    while snow < 50:
        n = rd.randint(-350,400)#random number chooser from a range
        u = rd.randint(-350,400)
        t.penup()
        t.goto(n,u)
        t.pendown()
        t.circle(2)
        snow = snow + 1
        print(n)
        print("runned")#checkpoints
        p = False
        


wn = trtl.Screen()
wn.mainloop()