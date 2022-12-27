# instead of writing the init function twice, they can inherit it from a "mother" class (superclass)

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def speak(self):
#         print("meow")

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def speak(self):
#         print("bark")


# superclass == upper level parent class
class Pet:  # general
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what to say")

class Cat(Pet):  # specific
    def __init__(self, name, age, color):
        super().__init__(name, age)  # references the superclass and executes the init function
        self.color = color

    def speak(self):
        print("meow")

    def show(self):
        print(f"I am {self.name}, {self.age} years old and I am {self.color}")

class Dog(Pet):  # specific
    def speak(self):
        print("bark")

class Fish(Pet):
    pass

p = Pet("Finn", 4)
p.show()
p.speak()

c = Cat("Luna", 3, "grey")
c.show()
c.speak()

d = Dog("Blu", 2)
d.show()
d.speak()

f = Fish("Bubbles", 13)
f.speak()