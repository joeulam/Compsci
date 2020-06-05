from course import Course
from student import Student

math = Course("Algebra I")
language = Course("Spanish I")
science = Course("Chemistry")
history = Course("U.S. History I")
phys_ed = Course("Physical Education I")

# TODO: Add two more courses of your choosing
comp_sci = Course("Computer Science")
english = Course("English Honors")

test_student = Student("Jill", "Sample")

test_student.add_course(math)
test_student.add_course(language)
test_student.add_course(science)
test_student.add_course(history)
test_student.add_course(comp_sci)

test_student2 = Student("Bill", "Sample")

test_student2.add_course(math)
test_student2.add_course(phys_ed)
test_student2.add_course(science)
test_student2.add_course(history)
test_student2.add_course(english)

# TODO Add a third test student and assign them four classes
test_student3 = Student("Joey", "Lam")
test_student3.add_course(language)
test_student3.add_course(history)
test_student3.add_course(english)
test_student3.add_course(science)
test_student3.add_course(comp_sci)
# TODO Add all the test students to a list of your own creation
student_list = [test_student, test_student2, test_student3]
# TODO print student_list
print(student_list)

# TODO iterate over each of the students in the list and print their names and course schedules.
    # Each iteration should:
        # print the student

for student in student_list:
  print(student.get_last_name() + ", " + student.get_first_name())
  for course in student.courses:
    print(course)
  print ('\n')