#######################################################################
# e-Portfolio Activity
# Develop a Python program and apply protected and unprotected variables 
# within it.
#######################################################################

''' 
Student Class:
- The Student class represents individual students and contains protected 
- variables for the student's name and grade, ensuring data privacy.
- Additionally, an unprotected variable stores the student's age.
- Methods within this class enable fetching and updating the student's grade.

Class Class:
- The Class class represents a class or course, with unprotected variables for 
  the class name and maximum number of students allowed.
- It maintains a list of enrolled students.
- Methods facilitate adding students to the class and computing the average grade 
  of all enrolled students.

Key Features:
- Utilization of protected variables (_name and _grade) within the Student class 
  to safeguard sensitive data.
- Usage of unprotected variables (age, class_name, max_students) in the Student 
  and Class classes for non-sensitive information.
- Implementation of methods to add students to a class while respecting the maximum 
  student limit and calculate the average grade of enrolled students.
- Demonstration of the program's functionality through the creation of student and 
  class instances, student enrollment, and output of class information including names 
  of enrolled students and average grade.
'''



class Student:
    def __init__(self, name, age, grade):
        self._name = name  # Protected variable: Stores the name of the student
        self.age = age  # Unprotected variable: Stores the age of the student
        self._grade = grade  # Protected variable: Stores the grade of the student

    def get_grade(self):
        return self._grade

    def set_grade(self, grade):
        self._grade = grade


class Class:
    def __init__(self, class_name, max_students):
        self.class_name = class_name  # Unprotected variable: Stores the name of the class
        self.max_students = max_students  # Unprotected variable: Stores the maximum number of students allowed in the class
        self.students = []  # List to store the students enrolled in the class

    def add_student(self, student):
        """
        Add a student to the class if the maximum limit is not reached.

        Args:
            student: Student object to be added to the class.

        Returns:
            bool: True if the student is added successfully, False otherwise.
        """
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        else:
            return False

    def get_average_grade(self):
        """
        Calculate the average grade of all students in the class.

        Returns:
            float: Average grade of all students in the class.
        """
        total_grade = 0
        for student in self.students:
            total_grade += student.get_grade()
        return total_grade / len(self.students)


# Creating students
student1 = Student("Alice", 18, 90)
student2 = Student("Bob", 17, 85)
student3 = Student("Charlie", 19, 88)

# Creating a class
class1 = Class("Math", 2)

# Adding students to the class
class1.add_student(student1)
class1.add_student(student2)
class1.add_student(student3)  # This won't be added because the class is full

print(f"Class: {class1.class_name}")
print(f"Maximum Students: {class1.max_students}")
print(f"Students in Class: {[student._name for student in class1.students]}")
print(f"Average Grade: {class1.get_average_grade()}")
