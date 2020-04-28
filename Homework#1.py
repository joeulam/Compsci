part = 1
supersize = True
total = 0
selected_sandwich = True
selected_drink = True
selected_fries = True 
sandwich_select = True
fries = True

order = []

sandwich_select = input("Do you want a sandwich? ")
if sandwich_select == "yes":
    sandwich_select = True
    part = 1
    sandwich = input("What type of sandwich would you like? Chicken, Beef, or Vegan patty ").lower()
else:
    print("You have choosen no sandwich")
    sandwich = "none"
    total += 0
    selected_sandwich = False
    part = 2
if part == 1: 
    if sandwich == "chicken" :
        order.append("chicken")
        total += 5.25
        part = 2 
    elif sandwich == "beef" :
        order.append("beef")
        total+= 6.25
        part = 2
    elif sandwich == "vegan patty" :
        order.append("vegan patty")
        total += 5.75
        part: 2 

    else:
        print("Please enter a valid sandwich type.")
        selected_sandwich = False
        part = 1  
if selected_sandwich == True:
  print("You ordered a " + sandwich + " sandwich." + "Your total comes to $" +str(total) + ".") 
if part == 2:
    print("We have small fries for $2, medium for $3, and large fries for $4")
    fries = input("Would you like fries? ")
    if fries == "yes":
        fries = True
        fries_size = input("What size fries do you want? ")
        if fries_size == "small":
            supersize = input("Would you like to supersize this?")
            if supersize =="yes":
                print("You have supersized this for $1.50")
                order.append("supersized fries")
                total += 1.50
                part = 3
                print("your total is now $" + str(total))
            elif supersize =="no":
                print("You have chosen regular small fries for $1 ")
                total += 1
                part = 3
                print("your total is now $" + str(total))
            else:
                print("Invalid response canceling order")
        elif fries_size == "medium":
            print("You have chosen medium fries for $1.50")
            order.append("medium fries")
            total += 1.50
            part = 3 
            print("Your total is now $" + str(total))
        elif fries_size == "large":
            print("You have chosen large fries for $2")
            order.append("large")
            total += 2
            part = 3
            print("Your total is now $" + str(total))
        else:
            print("Your answer is invalid canceling your order now")
    elif fries == "no":
        print("You have choosen no fries")
        order.append("no fries")
        fries_size = "none"
        total += 0
        selected_fries = False
        part = 3
    else:
        print("Invalid response canceling order")
drink_size = True
if part == 3:
    selected_drink = input("Do you want a drink? ")
    if selected_drink == "yes":
        print("We have 3 drink size. Small for 1.50, medium for 2.50, and large for 3.00")
        drink_size = input("What size do you want? ")
        if drink_size == "small":
            print("You have chosen a small drink for 1.00")
            order.append("small drink")
            total += 1.00 
            part = 4 
            print("Your total is now " + str(total))
        elif drink_size == "medium ":
            print("You have chosen a medium drink for 1.75")
            order.append("medium drink")
            total += 1.75
            part = 4
            print("Your total is now " + str(total))
        elif drink_size == "large":
            print("You have chosen a large drink for 2.25")
            order.append("large drink")
            total += 2.25
            part = 4
            print("Your total is " + str(total))
        else:
            print("Invalid response ending order")
    elif selected_drink == "no":
        print("You have choosen no drink")
        order.append("no drink")
        drink_size = "none"
        total += 0
        drink_size = False
        part = 4
        print("Your current order is " + str(sandwich) + " sandwich," + str(fries_size) + str(drink_size) +  " drink" + " total cost is " + str(total))
else:
    total += 0
ket = True
amount = True
if part == 4:
    ket = input("Do you want ketchup for .25 cent ")
    if ket =="yes":
        amount = input("How much packets do you want? ")
        amount = int(amount)
        if amount < 0 :
            print("error") 
        else:
            total += (amount * 0.25)
            print("Your final total is now " + str(total))
    elif ket == "no":
        print("Your total is now " + str(total))
    else:
        print("Error")

if selected_sandwich + selected_fries == True: 
        total += -1.00
        print(total)

if selected_sandwich == True and selected_drink == True and selected_fries == True and ket == True:
  print(order)
else:
    print(order)
