#Exercise 1: Favorite Numbers

my_fav_numbers = {7, 13, 21, 42}
my_fav_numbers.add(9)
my_fav_numbers.add(11)
my_fav_numbers.remove(11)
friend_fav_numbers = {3, 7, 9, 99}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print("Our favorite numbers:", our_fav_numbers)




#Exercise 2: Tuple

my_tuple = (1, 2, 3)

#my_tuple.append(4)  # AttributeError!
#my_tuple[0] = 10     # TypeError!




#Exercise 3: List Manipulation

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
apple_count = basket.count("Apples")

print(f"Apples appear {apple_count} times.")

basket.clear()

print("Final basket state:", basket)




#Exercise 4: Floats

mixed_sequence = []
for i in range(3, 11):
    mixed_sequence.append(i / 2)

print("Generated sequence:", mixed_sequence)



#Exercise 5: For Loop

print("All numbers from 1 to 20:")
for num in range(1, 21):
    print(num, end=" ")
print("\n")

print("Even numbers from 1 to 20:")
for num in range(1, 21):
    if num % 2 == 0:
        print(num, end=" ")
print()




#Exercise 6: While Loop

while True:
    name = input("Please enter your name: ").strip()
    if name.isdigit() or len(name) < 3:
        print("Invalid input, a proper name shouldn't be digits and must be at least 3 characters long.")
    else:
        print("thank you")
        break



#Exercise 7: Favorite Fruits

fav_fruits_input = input("Enter your favorite fruits separated by spaces : ")
fav_fruits_list = fav_fruits_input.lower().split()

chosen_fruit = input("Name a random fruit : ").strip().lower()

if chosen_fruit in fav_fruits_list:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")



#Exercise 8: Pizza Toppings

toppings = []
base_price = 10.0
topping_price = 2.50

while True:
    topping = input("Enter a pizza topping (or type 'quit' to finish): ").strip().lower()
    if topping == 'quit':
        break
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

total_price = base_price + (len(toppings) * topping_price)

print("\n--- Your Order Summary ---")
print(f"Toppings chosen: {', '.join(toppings) if toppings else 'None'}")
print(f"Total calculated price: ${total_price:.2f}")




#Exercise 9: Cinemax Tickets

ages_input = input("Enter the ages of everyone in your family buying a ticket (separated by spaces) : ")
ages = [int(age) for age in ages_input.split()]

total_cost = 0
for age in ages:
    if age < 3:
        total_cost += 0
    elif 3 <= age <= 12:
        total_cost += 10
    else:
        total_cost += 15

print(f"The total ticket cost for your family is: ${total_cost}")
print("-" * 40)

teenagers = ["Alex", "Jordan", "Taylor", "Morgan"]
allowed_attendees = []

print("Checking entry restriction eligibility for teenagers...")
for teen in teenagers:
    age = int(input(f"How old is {teen}? "))
    if 16 <= age <= 21:
        allowed_attendees.append(teen)
    else:
        print(f"-> {teen} is restricted from watching this film.")

print("\nFinal list of authorized attendees:", allowed_attendees)