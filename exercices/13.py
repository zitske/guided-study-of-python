#Write a Rectangle class that is initialized with the properties side and
#height, and a Circle class that is initialized with the radius property. Both
#classes must contain their area() methods that return the area of ​​each
#respective geometric figure. Then create a list of ten objects
#containing random objects of both classes and make a function that calculates the
#sum of the areas of all objects in the list.

class Rectangle:
    def __init__(self, side, height):
        self.side = side
        self.height = height

    def area(self):
        return self.side * self.height


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)


rectangles = [Rectangle(3, 4), Rectangle(5, 6), Rectangle(7, 8)]  # list of rectangles objects 
circles = [Circle(2), Circle(3), Circle(4)]  # list of circles objects 
objects_list = rectangles + circles  # list of all objects 


def sum_areas():  # function to calculate the sum of all areas in the list 
    total_area = 0   # variable to store the total area 

    for obj in objects_list:   # loop through all objects in the list 
        total_area += obj.area()   # add the area of each object to the total area variable

    return total_area   # return the total area calculated 


print("The sum of all areas is:", sum_areas())