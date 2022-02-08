
# Declare a Property

class Student:
    
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

s = Student('Steve')
s.name 

# Property Setter
class Student:
    
    def __init__(self, name):
        self.__name=name

    @property
    def name(self):
        return self.__name

    @name.setter   #property-name.setter decorator
    def name(self, value):
        self.__name = value


 s = Student('Steve')
>>> s.name 
'Steve'
>>> s.name = 'Bill'
'Bill'
# **Property Deleter***********************
class Student:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name=value
    
    @name.deleter   #property-name.deleter decorator
    def name(self, value):
        print('Deleting..')
        del self.__name

>>> s = Student('Steve')
>>> del s.name 
Deleting.. 
>>> s.name
# ******************************************************************

class Student:
    name = 'unknown' # class attribute
    def __init__(self):
        self.age = 20  # instance attribute

    @classmethod
    def tostring(cls):
        print('Student Class Attributes: name=',cls.name)

Student.tostring()
std=Student()
std.tostring()

# ***********************************

class Student:
    
    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age # instance attribute

    @classmethod
    def getobject(cls):
        return cls('Steve', 25)



std = Student.getobject()
print(std.name)
  
print(std.age)

# ***********************************
# The static method cannot access the class attributes or instance attributes. It will raise an error if try to do so.

# 
class Student:
    name = 'unknown' # class attribute
    
    def __init__(self):
        self.age = 20  # instance attribute

    @staticmethod
    def tostring():
        print('Student Class')

Student.tostring()
std = Student()
std.tostring()

