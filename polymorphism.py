"""
1. basic
2. polymorphism with classes : def function
3. polymorphism with classes : for loop
"""

# 1. basic
class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name+' says Woof!'
    
class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name+' says Meow!' 
    
niko = Dog('Niko')
felix = Cat('Felix')

print(niko.speak())
print(felix.speak())
# Niko says Woof!
# Felix says Meow!


# 2. polymorphism with classes : def function
class Dog():
    
    def __init__(self, name):
        self.name = name # attribute
        
    def speak(self):
        return self.name + " says whof!"
        
class Cat():
    
    def __init__(self, name):
        self.name = name # attribute
        
    def speak(self):
        return self.name + " says meow!"

def pet_speak(pet): # 'pet_speak' itself actually doesn't know whether it passes in Dog or Cat
    print(pet.speak())
        
mungmung = Dog("mungmung")
nabi = Cat("nabi")

pet_speak(mungmung)
pet_speak(nabi)
# mungmung says whof!
# nabi says meow!


# 3. polymorphism with classes : for loop
class Dog():
    
    def __init__(self, name):
        self.name = name # attribute
        
    def speak(self):
        return self.name + " says whof!"
        
class Cat():
    
    def __init__(self, name):
        self.name = name # attribute
        
    def speak(self):
        return self.name + " says meow!"

def pet_speak(pet): # 'pet_speak' itself actually doesn't know whether it passes in Dog or Cat
    print(pet.speak())
        
mungmung = Dog("mungmung")
nabi = Cat("nabi")

for pet in [mungmung, nabi]:
    
    print(type(pet))
    print(pet.speak())
# <class '__main__.Dog'>
# mungmung says whof!
# <class '__main__.Cat'>
# nabi says meow!



