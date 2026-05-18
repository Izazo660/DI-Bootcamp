#Challenge 1: Multiples of a Number

number = int(input("Enter a number : "))
length = int(input("Enter the length : "))
multiples_list = []

for i in range(1, length + 1):
    multiples_list.append(number * i)

print(multiples_list)




#Challenge 2: Remove Consecutive Duplicate Letters

user_word = input("Enter a word: ")
clean_string = ""

for char in user_word:
    if len(clean_string) == 0 or char != clean_string[-1]:
        clean_string += char

print(clean_string)