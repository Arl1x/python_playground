#!/usr/bin/env python3


class Dog:

    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)


# Instantiate the Dog object
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)

# Access the instance attributes
print("{} is {} and {} is {}.".format(
    philo.name, philo.age, mikey.name, mikey.age))

# Is Philo a mammal?
if philo.species == "mammal":
    print("{0} is a {1}!".format(philo.name, philo.species))

# Review Exercises (#1): The Oldest Dog
mark = Dog("Mark", 20)
jack = Dog("Jack", 18)
peeb = Dog("Peeb", 2)


def get_biggest_number(*args):
    return max(args)


print("The oldest dog is {} years old.".format(
    get_biggest_number(mark.age, jack.age, peeb.age)))

# call our instance methods
print(mikey.description())
print(mikey.speak("Gruff Gruff"))
