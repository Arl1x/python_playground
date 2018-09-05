#!/usr/bin/env python3


# Parent class
class Dog:

    # Class attribute
    species = 'mammal'
    is_hungry = True

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return self.name, self.age

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

    # instance method
    def eat(self):
    	self.is_hungry = False

    # instance method
    def walk(self):
    	return "{} is walking!".format(self.name)

# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


class Pets:

	dogs = []

	def __init__(self, dogs):
		self.dogs = dogs

	def walk(self):
		for dog in self.dogs:
			print(dog.walk())


my_dogs = [
	Bulldog("Tom", 6),
	RussellTerrier("Fletcher", 7),
	Dog("Larry", 9)
]

my_pets = Pets(my_dogs)

print("I have {} dogs.".format(len(my_pets.dogs)))
for dog in my_pets.dogs:
	dog.eat()
	print("{} is {}.".format(dog.name, dog.age))

print("And they're all {}s, of course.".format(dog.species))

are_my_dogs_hungry = False
for dog in my_pets.dogs:
	if dog.is_hungry:
		are_my_dogs_hungry = True

if are_my_dogs_hungry:
	print("My dogs are hungry.")
else:
	print("My dogs are not hungry.")

my_pets.walk()