execute_assignment = ""
execute_assignment = True
def assignment1():
  print("Assignment 1 completed")
  
assignment1()

def assignment2():
  return("Assignment 2 completed")
assignment2()

assignment2_result = assignment2()
print(assignment2_result)

while execute_assignment == True:
  assignment_number = input("")
  if assignment_number == ("1"):
    print(assignment1)
  elif assignment_number == ("2"):
    print(assignment2)
  elif assignment_number == ("quit"):
    print("Exiting")
  else: 
    print("Please enter 1,2,or quit")
else:
  print("Quitting")
  execute_assignment = False

