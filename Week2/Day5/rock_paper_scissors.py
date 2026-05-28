from game import Game

def get_user_menu_choice() :
    while True :
        print("\n--- Menu ---")
        print("1. Play a new game")
        print("2. Show scores")
        print("3. Quit")
        
        choice = input("Select an option (1-3) : ").strip()
        if choice in ["1", "2", "3"] :
            return choice
        print("Error : Invalid menu option. Please select 1, 2, or 3.")

def print_results(results) :
    print("\n====================")
    print("GAME SUMMARY")
    print("====================")
    print(f"Wins : {results['win']}")
    print(f"Losses : {results['loss']}")
    print(f"Draws : {results['draw']}")
    print("====================")
    print("Thank you for playing!")

def main() :
    results = {"win" : 0, "loss" : 0, "draw" : 0}
    
    print("==========================================")
    print("ROCK PAPER SCISSORS CHAMPIONSHIP")
    print("==========================================")
    
    while True :
        menu_choice = get_user_menu_choice()
        
        if menu_choice == "1" :
            game_instance = Game()
            game_output = game_instance.play()
            results[game_output] += 1
        elif menu_choice == "2" :
            print("\n--- Current Scoreboard ---")
            print(f"Wins : {results['win']} | Losses : {results['loss']} | Draws : {results['draw']}")
        elif menu_choice == "3" :
            print_results(results)
            break

if __name__ == "__main__" :
    main()