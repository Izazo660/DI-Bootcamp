#Exercise 1: Converting Lists into Dictionaries

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
new_dict = dict(zip(keys, values))

print(new_dict)




#Exercise 2: Cinemax #2

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_cost = 0

for name, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
        
    print(f"{name.capitalize()} pays : ${price}")
    total_cost += price

print(f"Total cost for the family : ${total_cost}")

print("\n Bonus : custom Family Input")
custom_family = {}
while True:
    name_input = input("Enter family member's name (or type 'done' to calculate) : ").strip()
    if name_input.lower() == 'done':
        break
    age_input = int(input(f"Enter age for {name_input}: "))
    custom_family[name_input] = age_input

custom_total = 0
for name, age in custom_family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    custom_total += price

print(f"custom family total ticket cost : ${custom_total}")




#Exercise 3: Zara

brand = {
    "name" : "Zara",
    "creation_date" : 1975,
    "creator_name" : "Amancio Ortega Gaona",
    "type_of_clothes" : ["men", "women", "children", "home"],
    "international_competitors" : ["Gap", "H&M", "Benetton"],
    "number_stores" : 7000,
    "major_color" : {
        "France" : "blue",
        "Spain" : "red",
        "US" : ["pink", "green"]
    }
}

brand["number_stores"] = 2  # Change value
clothes = ", ".join(brand["type_of_clothes"][:-1]) + f", and {brand['type_of_clothes'][-1]}"

print(f"Zara's clients look for clothes matching categories such as : {clothes}.")

brand["country_creation"] = "Spain"  # Add key

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

brand.pop("creation_date")  # Delete key

print("Last competitor :", brand["international_competitors"][-1])
print("Major colors in the US :", brand["major_color"]["US"])
print("Number of keys :", len(brand))
print("All keys :", list(brand.keys()))

more_on_zara = {
    "creation_date" : 1975,
    "number_stores" : 10000
}

brand.update(more_on_zara)
print("\nMerged brand dictionary:", brand)



#Exercise 4: Disney Characters

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

dict_1 = {character: index for index, character in enumerate(users)}
print("pattern 1 :", dict_1)

dict_2 = {index: character for index, character in enumerate(users)}
print("pattern 2 :", dict_2)

dict_3 = {character: index for index, character in enumerate(sorted(users))}
print("pattern 3 :", dict_3)