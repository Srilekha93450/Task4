import math  # Import the math module to access the precise value of pi

class Circle:
    def __init__(self, radii):
        self.__pi = math.pi  # Private member variable for pi
        self.radii = radii  # List of radii for the circles

    def area(self):
        areas = []  # List to store the calculated areas
        for radius in self.radii:  # Iterate through each radius in the list
            area = self.__pi * (radius ** 2)  # Calculate the area using the formula πr^2
            areas.append(area)  # Append the calculated area to the list
        return areas  # Return the list of areas

    def perimeter(self):
        perimeters = []  # List to store the calculated perimeters
        for radius in self.radii:  # Iterate through each radius in the list
            perimeter = 2 * self.__pi * radius  # Calculate the perimeter using the formula 2πr
            perimeters.append(perimeter)  # Append the calculated perimeter to the list
        return perimeters  # Return the list of perimeters


radii = [10, 501, 22, 37, 100, 999, 87, 351]  # List of radii for the circles
circle = Circle(radii)  # Create an instance of the Circle class with the list of radii
areas = circle.area()  # Calculate the areas of the circles
perimeters = circle.perimeter()  # Calculate the perimeters of the circles

# Print the calculated areas and perimeters
print("Areas:", areas)
print("Perimeters:", perimeters)
