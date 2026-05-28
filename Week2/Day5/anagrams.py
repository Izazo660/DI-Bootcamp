from anagram_checker import AnagramChecker

def clean_and_validate_input(user_input) :
    cleaned = user_input.strip()
    if not cleaned :
        print("Error : Input cannot be empty.")
        return None
    if len(cleaned.split()) > 1 :
        print("Error : Only a single word is allowed. Do not include spaces.")
        return None
    if not cleaned.isalpha() :
        print("Error : Only alphabetic characters are allowed.")
        return None
    return cleaned

def main() :
    chemin_sowpods = r"C:\Users\ierri\Documents\DI-Bootcamp\Week2\Day5\sowpods.txt"
    checker = AnagramChecker(chemin_sowpods)
    
    while True :
        print("\n--- Main Menu ---")
        print("1. Input a word to find anagrams")
        print("2. Exit program")
        
        choice = input("Select an option (1-2) : ").strip()

        if choice == "2" :
            print("\nThank you for using Anagram Solver. Goodbye!")
            break
        elif choice == "1" :
            raw_word = input("\nEnter your word : ")
            validated_word = clean_and_validate_input(raw_word)
            
            if validated_word is None :
                continue
                
            is_valid = checker.is_valid_word(validated_word)
            
            print("\n" + "="*30)
            print(f"YOUR WORD : \"{validated_word.upper()}\"")
            
            if is_valid :
                print("This is a valid English word.")
            else :
                print("Note : This word was not found in the official word list.")
                
            found_anagrams = checker.get_anagrams(validated_word)
            
            if found_anagrams :
                anagrams_str = ", ".join(found_anagrams)
                print(f"Anagrams for your word : {anagrams_str}.")
            else :
                print("No valid anagrams were found for this word.")
            print("="*30)
        else :
            print("Invalid Choice! Please enter either 1 or 2.")

if __name__ == "__main__" :
    main()