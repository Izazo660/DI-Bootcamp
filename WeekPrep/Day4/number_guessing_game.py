import random

def number_guessing_game():
    random_number = random.randint(1, 100)
    max_attempts = 7
    for i in range(max_attempts):
        guess = int(input("Guess the number : "))
        if guess < random_number:
            print("Too low!")
        elif guess > random_number:
            print("Too high!")
        elif guess == random_number:
            return "Good job you have found the secret number !"
            break
    return f"Sadly you have failed and the correct number was : {random_number}"

print(number_guessing_game())