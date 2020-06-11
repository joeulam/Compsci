execute_assignment = ""
execute_assignment = True

def assignment1():
  print("Assignment 1 Completed")

assignment1()

def assignment2():
  return ("Assignment 2 Completed")

assignment2()
assignment2_result = assignment2()

print(assignment2_result)

while execute_assignment == True:
  assignment_number = input("Enter 1,2,or Quit ")
  if assignment_number == ("1"):
    print("Assignment 1 Completed")
  elif assignment_number == ("2"):
    print("Assignment 2 Completed")
  elif assignment_number == ("Quit"):
    print("Leaving")
    execute_assignment = False
  else:
    print("Enter 1,2,or Quit ")
else:
  print("Quitting")