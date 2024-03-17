# Tutorial Lab 1: Creating a Class

1. Let’s now get some practice using classes in Python. For our scenario around BMI values, we have started to relate them to people. In this exercise, we will start to put together the class file to represent a person. Do not copy and past this code as the double quotes may not be accurately represented in the python file on the left.<br><br>

```
class Person:
    “””Represents a generic Person.”””

print(type(Person))
print(Person)
```
Run this code sample with the Python drop down menu option.
<br>
2. This code creates a new user-defined type (class), called Person and then outputs its type.<br>
<class 'type’>
<class 'main.Person’>
<br>
3. Using the type() method in print(), tells us the object is a type but printing the class itself indicates it is a main.Person and shows it as a class
4. However, this class isn’t really useful because it’s just a class name and that is it. In order to be useful, it must have some member data fields (attributes) to store information specific to the instance of a Person you will create later. Member functions(methods) will be covered in the next unit
5. Modify your code to look like this:
```
class Person:
     """Represents a generic Person."""
     def __init__(self, first, last, weight, height):
          self.first_name = first
          self.last_name = last
          self.weight_in_lbs = weight
          self.height_in_inches = height

print(Person)
```
6. What we have changed here is to add an initializer (constructor) that helps us set up some member data variables for first name, last name, weight, and height. When we create a new instance of an object to represent an actual person, we will provide the values for the variables and the constructor will initialize the new object with these variables. Let’s do that next.
