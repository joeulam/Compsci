part = 0 
total = 0
selected_sandwich = True
selected_drink = True
selected_fries = True 
sandwich_select = False
fries = False
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
        total += 5.25
        part = 2 
    elif sandwich == "beef" :
        total+= 6.25
        part = 2
    elif sandwich == "vegan patty" :
        total += 5.75
        part: 2 
    else:
        print("Please enter a valid sandwich type.")
        selected_sandwich = False
        part = 1  
if selected_sandwich == True:
  print("You ordered a " + sandwich + " sandwich." + "Your total comes to $" +str(total) + ".") 
selected_drink = True
drink_size = True
if part == 2:
  drink_size = input("Do you want a drink? ")
  if drink_size == "yes":
    print("We have 3 drink size. Small for 1.50, medium for 2.50, and large for 3.00")
    drink_size = input("What size do you want?")
    if drink_size == "small":
      print("You have chosen a small drink for 1.50")
      total += 1.50
      part = 3  
      print("Your total is now " + str(total))      
    elif drink_size == "medium ":
      print("You have chosen a medium drink for 2.50")
      total += 2.50
      part = 3
      print("Your total is now " + str(total))
    elif drink_size == "large":
      print("You have chosen a large drink for 3.00")
      total += 3
      part = 3
      print("Your total is " + str(total))
    else:
      print("Invalid response ending order")
  else:
      print("You have choosen no drink")
      drink_size = "none"
      total += 0
      selected_drink = False
      part = 3
if part == 3:
    print("We have small fries for $2, medium for $3, and large fries for $4")
    fries = input("Would you like fries? ")
    if fries == "yes":
        fries = True
        fries_size = input("What size fries do you want? ")
        if fries_size == "small":
            print("You have chosen small fries for $2 ")
            total += 2
            part = 3
            print("your total is now " + str(total))
        elif fries_size == "medium":
            print("You have chosen medium fries for $3")
            total += 3
            part = 3 
            print("Your total is now " + str(total))
        elif fries_size == "large":
            print("You have chosen large fries for $4")
            total += 4 
            part = 3
            print("Your total is now " + str(total))
        else:
            print("Your answer is invalid canceling your order now")
    elif fries == "no":
        print("You have chosen no fries")
        print("Your current order is " + str(sandwich) + "sandwich and" + str(fries_size) + "total cost is " + str(total))      
    else:
        print("Invalid response canceling order")

