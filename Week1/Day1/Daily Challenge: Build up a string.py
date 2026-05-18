import random

# 1. Ask for User Input
user_string = input("Enter a string of exactly 10 characters: ")



# 2. Check the Length of the String
if len(user_string) < 10:
    print("String not long enough.")
elif len(user_string) > 10:
    print("String too long.")
else:
    print("Perfect string")
    print("-" * 30) # Visual separator



# 3. Print the First and Last Characters
print(f"First character: {user_string[0]}")
print(f"Last character: {user_string[-1]}")
print("-" * 30)



# 4. Build the String Character by Character
current_string = ""
print("Progressive printing:")
for char in user_string:
    current_string += char
    print(current_string)
print("-" * 30)



# 5. Bonus: Jumble the String
char_list = list(user_string)
random.shuffle(char_list)

jumbled_string = "".join(char_list)
print(f"Jumbled string: {jumbled_string}")