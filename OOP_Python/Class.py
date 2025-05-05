class Car : 
    def __init__(self,user_brand,user_model):
        self.brand  = user_brand #user_brand and user_model are attributes 
        self.model = user_model
result = Car("Toyota","Ferari")   #Function is called here 
print(result.brand)     #Here brand value is printed 
print(result.model)      #Here model value is printed 
    #   Car → is a class (a blueprint).
    # result → is an object (a real car created using the blueprint).
    # An object can access the data (attributes) set by the constructor.
    
    
    
class Dog:
        def __init__(self,breed,gender): #Tis is Constructor
            # self refers to the current object (instance) of the class.
            self.breed = breed 
            self.gender = gender
dog= Dog("Pitbul","Male")   # Creating a obj
print(dog.breed)
print(dog.gender)

#Adding one more function    
class animal:
    def __init__(self,bird,gender):
         self.bird = bird
         self.gender = gender
    def Full_name(self):
        return f"{self.bird}{self.gender}"
result = animal("peacock","Female")
print(result.bird)
print(result.gender)
# print(result.Full_name)     This will produce Error
#Why Full_name() is Not Called Automatically:
# Python doesn't automatically call any methods (like Full_name) 
# when the object is created unless you explicitly (clearly) do so within the constructor.
# The constructor (__init__) is specifically for setting up the object’s initial state.
         
print(result.Full_name())