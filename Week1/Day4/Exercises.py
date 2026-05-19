from random import randint
#Exercise 1: What Are You Learning?

def display_message():
    return "I am learning about functions in Python."

print(display_message())


#Exercise 2: What’s Your Favorite Book?

def favorite_book(title):
    return f"One of my favorite books is {title}"

print(favorite_book("Omniscient reader viewpoint"))


#Exercise 3: Some Geography

def describe_city(city, country = "Unknown"):
    return f"{city} is in {country}"


print(describe_city("Reykjavik", "Iceland"))
print(describe_city("Paris"))


#Exercise 4: Random

def random(a):
    b = randint(1, 100)
    if a == b:
        return "Success!"
    else:
        return f"Fail! Your number: {a}, Random number: {b}"


print(random(52))


#Exercise 5: Let’s Create Some Personalized Shirts!

def make_shirt(size = "large", text = "I love Python"):
    return f"The size of the shirt is {size} and the text is {text}."

print(make_shirt())
print(make_shirt("medium"))
print(make_shirt("medium", "Awesome"))


#Exercise 6: Magicians…

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
new_magician_names = []

def make_great(tab):
    for i in tab:
        new_magician_names.append(i + " " + "the great")

make_great(magician_names)

def show_magicians(tab):
    for i in tab:
        print(i)

show_magicians(new_magician_names)



#Exercise 7: Temperature Advice
import random

def get_random_temp(month):
    if month in [12, 1, 2]:
        return random.uniform(-10.0, 5.0)
    elif month in [3, 4, 5]:
        return random.uniform(6.0, 18.0)
    elif month in [6, 7, 8]:
        return random.uniform(19.0, 40.0)
    elif month in [9, 10, 11]:
        return random.uniform(6.0, 18.0)

def main():
    month_input = int(input("Enter the current month as a number : "))
    if month_input < 1 or month_input > 12:
        return "Invalid month! Please enter a number between 1 and 12."
    temp = get_random_temp(month_input)
    print(f"The temperature right now is {round(temp, 1)} degrees Celsius.")
    if temp < 0:
        return "Brrr, that’s freezing! Wear some extra layers today."
    elif 0 <= temp < 16:
        return "Quite chilly! Don’t forget your coat."
    elif 16 <= temp < 23:
        return "Nice weather."
    elif 24 <= temp < 32:
        return "A bit warm, stay hydrated."
    else:
        return "It’s really hot! Stay cool."

    
print(main())