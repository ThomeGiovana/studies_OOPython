# class atributes != instance atributes or object atributes
# class atributes are specific to the class, not to an instance or an object of that class
# class methods follow the same idea

class Person:
    # it doesn't change from person to person
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        # Person.number_of_people += 1
        Person.add_person()

    # decorator to denote that this specific method is a class method
    @classmethod
    def number_of_people(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person("Gio")
p2 = Person("Ge")

print(p1.number_of_people)
print(Person.number_of_people)

# you can change the number of people outside the class
# Person.number_of_people = 8
# print(Person.number_of_people)