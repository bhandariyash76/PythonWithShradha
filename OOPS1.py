# oops in python

# to map with real world scenarios we started using objects in code
# this is called object oriented programming

# to reduce redundancy in code we use classes and objects and reuse the code

# to make an object we have to create a class first which is a blueprint of the object

# class & ibject in python
# class is a blueprint of the object

# creating a class

class Student:
    name = "John"

# creating an object of the class(instances of the class)

student1 = Student()
print(student1.name)

class Car:
    color = "Red"

car1 = Car()
print(car1.color)

# constructor in python
# __init__ function all classes have a functional called __init__, which is always executed when the class is being initiated. it is invoked at the time of object creation(execute hota h)

class Student:
    name = "John"
    # default constructor
    def __init__(self):
        print(self)
        print("This is a constructor")
    
#constructor always takes argument which is self, self is a reference to the current instance of the class, and is used to access variables that belongs to the class
student1 = Student()
print(student1)

class Student:
    # parameterized constructor
    def __init__(self, name):
        self.name = name # self.name is an instance variable, name is a local variable

student1 = Student("John")
print(student1.name)

# the self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class. it is used to differentiate between instance variables and local variables.

student2 = Student("Alice")
print(student2.name)

# all the data stored in the instance variable is called attributes of the class, and the functions defined in the class are called methods of the class.

 
 # Instance attributes
 # we have class attributes and instance attributes, class attributes are shared by all instances of the class, while instance attributes are unique to each instance of the class.

# methods : in python methods are function that belong to objects, they are defined inside a class and can be called on an object of that class.

