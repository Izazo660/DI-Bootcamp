import random

class Game :
    def get_user_item(self) :
        while True :
            choice = input("Select an item (rock, paper, scissors) : ").strip().lower()
            if choice in ["rock", "paper", "scissors"] :
                return choice
            print("Error : Invalid item choice. Please try again.")

    def get_computer_item(self) :
        return random.choice(["rock", "paper", "scissors"])

    def get_game_result(self, user_item, computer_item) :
        if user_item == computer_item :
            return "draw"
        
        winning_rules = {
            "rock" : "scissors",
            "paper" : "rock",
            "scissors" : "paper"
        }
        
        if winning_rules[user_item] == computer_item :
            return "win"
        else :
            return "loss"

    def play(self) :
        user_choice = self.get_user_item()
        computer_choice = self.get_computer_item()
        result = self.get_game_result(user_choice, computer_choice)
        
        print("\n--- Game Outcome ---")
        print(f"Your choice : {user_choice}")
        print(f"Computer choice : {computer_choice}")
        print(f"Result : You got a {result}!")
        print("--------------------")
        
        return result