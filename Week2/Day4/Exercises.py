#Exercise 1: Random Sentence Generator

import random
import os

def get_words_from_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            words_list = content.split()
            return words_list
    except FileNotFoundError:
        print(f"\nError : The file at '{file_path}' was not found.")
        print("Please make sure 'words.txt' exists in your directory.")
        return []


def get_random_sentence(length):
    file_path = "Week2/Day4/words.txt"
    words = get_words_from_file(file_path)
    if not words:
        return None
    selected_words = [random.choice(words) for _ in range(length)]
    sentence = " ".join(selected_words).lower()
    sentence = sentence.capitalize() + "."
    return sentence


def main():
    print("WELCOME TO THE RANDOM SENTENCE GENERATOR")
    print("This program reads a word list file and builds")
    print("a random sentence based on your preferred length.")
    user_input = input("How many words long should your sentence be ? (Between 2 and 20): ")
    try:
        length = int(user_input)
        if 2 <= length <= 20:
            generated_sentence = get_random_sentence(length)
            if generated_sentence:
                print("\nYour Generated Sentence :")
                print(generated_sentence)
        else:
            print("\nInput Error : The number must be between 2 and 20.")
            
    except ValueError:
        print("\nInput Error : That is not a valid integer. Enter a number.")

if __name__ == "__main__":
    main()




#Exercise 2: Working with JSON

import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)


salary_value = data["company"]["employee"]["payable"]["salary"]
print(f"Extracted Salary Value : {salary_value}")


data["company"]["employee"]["birth_date"] = "1994-05-27"

output_file = "modified_employee.json"

with open(output_file, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

print(f"\nSuccess ! The modified data has been saved to '{output_file}'.")