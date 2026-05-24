#Exercise 1: Cats

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Step 1: Create cat objects
cat1 = Cat("Pablo", 3)
cat2 = Cat("Ricardo", 5)
cat3 = Cat("Felix", 4)

# Step 2: Create a function to find the oldest cat
def find_oldest_cat(cat1, cat2, cat3):
    if cat1.age > cat2.age and cat1.age > cat3.age:
        return cat1 
    if cat2.age > cat1.age and cat2.age > cat3.age:
        return cat2
    else:
        return cat3

# Step 3: Print the oldest cat's details

oldest = find_oldest_cat(cat1, cat2, cat3)

print(f"The oldest cat name is {oldest.name} and he has {oldest.age} years old.")



#Exercise 2 : Dogs

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    
    def bark(self):
        print(f"{self.name} goes woof!")
    
    def jump(self):
        x = self.height * 2
        print(f"{self.name} jumps {x} cm high!")


davids_dog = Dog("Barky", 120)
sarahs_dog = Dog("Poutif", 160)

print(davids_dog.name)
print(davids_dog.height)
print(sarahs_dog.name)
print(sarahs_dog.height)
davids_dog.bark()
davids_dog.jump()
sarahs_dog.bark()
sarahs_dog.jump()




#Exercise 3 : Who’s the song producer?

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for i in self.lyrics:
            print(i)

stairway = Song(["There's a lady who's sure", "all that glitters is gold", "and she's buying a stairway to heaven"])
stairway.sing_me_a_song()



#Exercise 4 : Afternoon at the Zoo

class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
        self.grouped_animals = {}

    def add_animal(self, *args):
        for new_animal in args:
            if new_animal not in self.animals:
                self.animals.append(new_animal)
                print(f'"{new_animal}" has been added to the zoo.')
            else:
                print(f'"{new_animal}" is already in the zoo!')

    def get_animals(self):
        print(f"\nAnimals in {self.zoo_name}")
        if not self.animals:
            print("The zoo is currently empty.")
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f'\n"{animal_sold}" has been sold.')
        else:
            print(f'\n"{animal_sold}" is not in the zoo.')

    def sort_animals(self):
        self.animals.sort()
        self.grouped_animals = {}
        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter not in self.grouped_animals:
                self.grouped_animals[first_letter] = [animal]
            else:
                self.grouped_animals[first_letter].append(animal)
        print("\nAnimals have been successfully sorted and grouped.")
        return self.grouped_animals

    def get_groups(self):
        print(f"\n{self.zoo_name} Groups Structure")
        if not self.grouped_animals:
            print("Please run sort_animals() first to build groups.")
        else:
            for letter, list_of_animals in self.grouped_animals.items():
                print(f"{letter}: {list_of_animals}")


# Step 2: Create a Zoo instance
brooklyn_safari = Zoo("Brooklyn Safari")

# Step 3: Use the Zoo methods
brooklyn_safari.add_animal("Giraffe", "Bear", "Baboon", "Cougar", "Cat", "Lion")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()