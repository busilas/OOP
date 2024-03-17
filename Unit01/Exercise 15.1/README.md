# Exercise 15.1

Write a definition for a class named Circle with attributes center and radius, where center is a Point object and radius is a number.<br>
Instantiate a Circle object that represents a circle with its center at (150,100) and radius 75.
Write a function named ```point_in_circle``` that takes a Circle and a Point and returns True if the Point lies in or on the boundary of the circle.<br>
Write a function named ```rect_in_circle``` that takes a Circle and a Rectangle and returns True if the Rectangle lies entirely in or on the boundary of the circle.<br>
Write a function named ```rect_circle_overlap``` that takes a Circle and a Rectangle and returns True if any of the corners of the Rectangle fall inside the circle. Or as a more challenging version, return True if any part of the Rectangle falls inside the circle.<br><br><br>



Remove any printing from your code and then add the following to the end:

```
def main():
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 50.0
    box.corner.y = 50.0

    circle = Circle
    circle.center = Point()
    circle.center.x = 150.0
    circle.center.y = 100.0
    circle.radius = 75.0

    print(point_in_circle(box.corner, circle))
    print(rect_in_circle(box, circle))
    print(rect_circle_overlap(box, circle))


if __name__ == '__main__':
    main()
```


