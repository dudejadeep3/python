# using classes we can create our own data type.
# used to create real world objects

from student import Student

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Jacky", "Engineering", 3.8, True)
print(student1)
print(student1.name)
print(student1.gpa)
print(student2.gpa)

print(student1.on_honor_roll())
print(student2.on_honor_roll())