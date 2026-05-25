#Exercise 1: Pets

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'



bengal_obj = Bengal("Ricardo", 1)
chartreux_obj = Chartreux("Pedro", 6)
siamese_obj = Bengal("Felix", 4)

all_cats = [bengal_obj, chartreux_obj, siamese_obj]

sara_pets = Pets(all_cats)

sara_pets.walk()



#Exercise 2: Dogs

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking."

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        speed1 = self.run_speed() * self.weight
        speed2 = other_dog.run_speed() * other_dog.weight
        if speed1 > speed2:
            return f"{self.name} won."
        else:
            return f"{other_dog.name} won."

# Step 2: Create dog instances
dog1 = Dog("Rocky", 8, 140)
dog2 = Dog("Midro", 2, 180)
dog3 = Dog("Ferit", 5, 110)


# Step 3: Test dog methods
print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))


#Exercise 3: Dogs Domesticated

import random

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dog_names = [dog.name for dog in args]
        all_names = [self.name] + dog_names
        names_str = ", ".join(all_names)
        print(f"{names_str} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")

# Test PetDog methods
my_dog = PetDog("Fido", 2, 10)
my_dog.train()

buddy_dog = Dog("Buddy", 3, 15)
max_dog = Dog("Max", 4, 12)
my_dog.play(buddy_dog, max_dog)

my_dog.do_a_trick()




#Exercise 4: Family and Person Classes

class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""
    
    def is_18(self):
        if self.age >= 18:
            return True
        else:
            return False
        

class Family(Person):
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []
    
    def born(self, first_name, age):
        new_person = Person(first_name, age)
        new_person.last_name = self.last_name
        self.members.append(new_person)
        print(f"{first_name} {self.last_name} was added to the family.")

    def check_majority(self, first_name):
        for person in self.members:
            if person.first_name == first_name:
                if person.is_18():
                    return "You are over 18, your parents Jane and John accept that you will go out with your friends"
                else:
                    return "Sorry, you are not allowed to go out with your friends."
            else:
                return "This person isn't in the family"

    def family_presentation(self):
        print(f"\nThe {self.last_name} Family Presentation")
        for person in self.members:
            print(f"- {person.first_name} {person.last_name}, Age: {person.age}")
        print("-" * 40)


smith_family = Family("Smith")

smith_family.born("Alice", 22)
smith_family.born("Bob", 15)
smith_family.born("Charlie", 18)

smith_family.family_presentation()

print("Checking status for Alice:")
smith_family.check_majority("Alice")

print("\nChecking status for Bob:")
smith_family.check_majority("Bob")