class Circle:
    
    # Class Object Attribute
    pi = 3.14

    # Circle gets instantiated with a radius (default is 1)
    def __init__(self, radius=1): # Attribute
        self.radius = radius 
        self.area = radius * radius * Circle.pi # (means calling a class object attribute)

    # Method for resetting Radius
    def setRadius(self, new_radius): # Method
        self.radius = new_radius
        self.area = new_radius * new_radius * self.pi

    # Method for getting Circumference
    def getCircumference(self): # Method
        return self.radius * self.pi * 2


c = Circle()

print('Radius is: ',c.radius)
print('Area is: ',c.area)
print('Circumference is: ',c.getCircumference())
# Radius is:  1
# Area is:  3.14
# Circumference is:  6.28

c.setRadius(2)

print('Radius is: ',c.radius)
print('Area is: ',c.area)
print('Circumference is: ',c.getCircumference())
# Radius is:  2
# Area is:  12.56
# Circumference is:  12.56