"""
1.1 polymorphism : basic
1.2 polymorphism : for loop
1.3 polymorphism : def
2. inheritance
3. abstract method
"""

# 1.1 Polymorphism - Basic code with two classes(!= type, therefore different types of classes repectively)
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

lucky = Dog("lucky")
nabi = Cat("nabi")

print(lucky.speak())
print(nabi.speak())
# lucky says whof!
# nabi says meow!


# 1.2 Polymorphism (1) : Implementing with for loop
"""
Polymorphism with class methods:
Below code shows how python can use two different class types, in the same way. We create a for loop that iterates through a tuple of objects. Then call the methods without being concerned about which class type each object is. We assume that these methods actually exist in each class.
"""
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

lucky = Dog("lucky")
nabi = Cat("nabi")

for pet in [lucky, nabi]:
    print((pet.speak()))
# lucky says whof!
# nabi says meow!


# 1.3 Polymorphism (2) : Implementing Polymorphism with a Function
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
 
lucky = Dog("lucky")
nabi = Cat("nabi")

pet_speak(lucky) 
pet_speak(nabi) 
# lucky says whof!
# nabi says meow!


# 2. Inheritance  : speak함수 외에도 부모클래스를 상속하여 다른 함수들도 사용 가능하게 연결
class Animal():
    
    def __init__(self):
        pass
    
    def who_am_i(self):
        print("I am an animal")
        
    def eat(self):
        print("I am eating")

class Dog(Animal): # interit from the basic class
    
    def __init__(self, name):
        Animal.__init__(self)  # inherit and have access to all methods you want
        self.name = name
      
    def speak(self):
        return self.name + " says woof!"

class Cat(Animal): # interit from the basic class
    
    def __init__(self, name):
        Animal.__init__(self)  # inherit and have access to all methods you want
        self.name = name
      
    def speak(self):
        return self.name + " says woof!"
        
lucky = Dog('lucky')
nabi = Dog('nabi')

print(lucky.speak())
print(nabi.speak())
# lucky says whof!
# nabi says meow!


# 3. Abstract Method : No need to write Animal.__init__
class Animal:
    def __init__(self, name):    # Constructor of the class
        self.name = name

    def speak(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    
    def speak(self):
        return self.name+' says Woof!'
    
class Cat(Animal):

    def speak(self):
        return self.name+' says Meow!'
    
lucky = Dog('lucky')
nabi = Dog('nabi')

print(lucky.speak())
print(nabi.speak())
# lucky says whof!
# nabi says meow!