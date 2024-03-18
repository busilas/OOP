#######################################################################
# e-Portfolio Activity
# Develop a Python program and apply protected and unprotected variables 
# within it.
#######################################################################

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
