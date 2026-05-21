#Challenge 1 : Sorting

user_input = input("Give us a string of words with each word separated by commas :")

words_list = user_input.split(",")

words_list.sort()

result_string = ",".join(words_list)

print(result_string)


#Challenge 2: Longest Word

def longest_word(sentence):
    words = sentence.split()
    current_longest = words[0]
    for word in words:
        if len(word) > len(current_longest):
            current_longest = word
    return current_longest


print(longest_word("Margaret's toy is a pretty doll."))
print(longest_word("A thing of beauty is a joy forever."))
print(longest_word("Forgetfulness is by all means powerless!"))