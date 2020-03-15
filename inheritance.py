# 1. inherit from the basic class -> get all access to all methods you want
# 2. can overwrite
# 3. add more methods

class Animal():
    
    def __init__(self):
        print("ANIMAL CREATED")
    
    def who_am_i(self):
        print("I am an animal")
        
    def eat(self):
        print("I am eating")

class Dog(Animal): # inherit from the basic class
    
    def __init__(self):
        Animal.__init__(self)  # inherit and have access to all methods you want
        print("Dog Created")
    
    def eat(self): 
        print("I am a dog and eating") # overwrite
        
    def bark(self):
        print("WOOF!") # add new methods

mydog = Dog()
# ANIMAL CREATED
# Dog Created

mydog.who_am_i() # interit
# I am an animal

mydog.eat() # overwrite
# I am a dog and eating

mydog.bark() # add a new method
# WOOF!
