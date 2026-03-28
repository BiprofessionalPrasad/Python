# -*- coding: utf-8 -*-
"""
Created on Thu May 16 15:59:23 2019

@author: pgaiton
"""

#### ------------- creating a dog class ------------- ####
class Dog():
    """Represents a dog."""
    
    def __init__(self,name):
        """initiate Dog object"""
        self.name = name
        
    def sit(self):
        """Simulate sitting"""
        print(self.name + " is sitting.")
        
my_dog = Dog('Peso')

type(my_dog)

print(my_dog.name + " is a great dog! ")


#### ------------- inheritance ------------- ####
class SARDog(Dog):
    """Represents a search dog."""
    
    def __init__(self,name):
        """initiate the SARDog object"""
        super().__init__(name)
        
    def search(self):
        """Simulate searching"""
        print(self.name + " is searching.")
        
my_dog = SARDog('Willie')

type(my_dog)

print(my_dog.name + " is a search dog.")
my_dog.sit()
my_dog.search()


# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 16:41:46 2020

@author: pgaiton
"""

class person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
        
me = person('Prasad',39)
type(me)
print('I am '+me.name+' aged ' + str(me.age))

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 16:27:15 2020

@author: pgaiton
"""

class Person:
    def __init__(self,fn,ln):
        self.fn = fn
        self.ln = ln
        
    def printname(self):
        print(self.fn,self.ln)
    
    def myfunc(self):
        print('my name is '+ self.fn +' '+self.ln)

class Student(Person):
    pass
        
me = Student('Prasad','Gaitonde')
me.myfunc()