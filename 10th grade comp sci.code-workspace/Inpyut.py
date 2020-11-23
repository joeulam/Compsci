t = 0
x = 0
pp = 0

x = input(" Enter a number ")
t = input("Enter another number")

while pp < 1: 
    if (int(x) % int(t) == 0):
        print("Its compatible")
        pp = pp + 1 
    if (int(x) % int(t) != 0):
        print("Its incampatible")
        x = input(" Enter a number ")
        t = input("Enter another number")
