class Farm:
    def __init__(self, farm_name):
        self.farm_name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, count=1):
        animal_type = animal_type.strip().lower()
        if animal_type in self.animals:
                self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    def get_info(self):
        info_str = f"{self.farm_name}'s farm\n\n"
        for animal, count in self.animals.items():
             info_str += f"{animal:<12} : {count}\n"
        info_str += f"\n    E-I-E-I-O!"
        return info_str

# Test the code 
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
#output:
# McDonald's farm

# cow : 5
# sheep : 2
# goat : 12

#     E-I-E-I-0!