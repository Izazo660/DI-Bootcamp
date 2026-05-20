import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist)

### YOUR CODE STARTS FROM HERE ###

GALLOWS_STAGES = [
    """
     ------
     |    |
     |    
     |   
     |    
     |   
    ---
    """,
    """
     ------
     |    |
     |    O
     |   
     |    
     |   
    ---
    """,
    """
     ------
     |    |
     |    O
     |    |
     |    
     |   
    ---
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |    
     |   
    ---
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |    
     |   
    ---
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / 
     |   
    ---
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |   
    ---
    """ 
]

incorrect_guesses = 0
guessed_letters = set()
hidden_word = [char if char == " " else "*" for char in word]

print("Welcome to Hangman !")

while incorrect_guesses < 6:
    print(GALLOWS_STAGES[incorrect_guesses])
    print("Word to guess: " + "".join(hidden_word))
    print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
    if "*" not in hidden_word:
        print(f"\nCongratulations ! You guessed the word: '{word}'!")
        break
    guess = input("Guess a letter: ").lower().strip()
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input! Please enter exactly one alphabetical letter.")
        continue
    if guess in guessed_letters:
        print(f"You already guessed the letter '{guess}'. Try a different one!")
        continue
    guessed_letters.add(guess)
    if guess in word:
        print(f"Good job ! '{guess}' is in the word.")
        for index, char in enumerate(word):
            if char == guess:
                hidden_word[index] = guess
    else:
        incorrect_guesses += 1
        remaining_parts = 6 - incorrect_guesses
        print(f"Wrong choice ! '{guess}' is not in the word.")
        if remaining_parts > 0:
            print(f"You have {remaining_parts} body parts remaining before the gallows is full.")

if "*" in hidden_word:
    print(GALLOWS_STAGES[6])
    print("Game Over! You've been hanged.")
    print(f"The correct word was : '{word}'")