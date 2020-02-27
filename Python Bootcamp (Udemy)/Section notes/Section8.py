class Dog():
    #CLASS OBJECT ATTRIBUTE
    #SAME FOR ANY INSTANCE OF A CLASS
    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name
    #OPERATIONS/ACTIONS (METHODS)
    def bark(self, color):
        print(f"WOOF! My name is {self.name} and I have {color} fur!")

my_dog = Dog('Portie', 'Dante')
print(my_dog.name)
print(my_dog.species)
my_dog.bark('black')

class Animal():

    def __init__(self):
        print("ANMIAL CREATED")

    def who_ami_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

class Dog2(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

class Dog3():
    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + "says woof!"

class Cat():
    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + "says meow!"

niko = Dog3("niko")
felix = Cat("felix")
print(niko.speak())
print(felix.speak())

for pet in [niko, felix]:
    print(type(pet))
    print(type(pet.speak()))

def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)

# ABSTACT CLASS 
class Animal2():
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstarct method")

class Dog4(Animal2):
    def speak(self):
        return self.name+ " says woof!"

niko = Dog4("niko")
Dog4.speak(niko)

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"{self.title} by {self.author}"
    def __len__(self):
        return self.pages
    def __del__(self):
        print("A book object has been deleted")