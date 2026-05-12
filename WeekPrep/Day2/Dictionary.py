tab = [("name", "Elie"), ("job", "Instructor")]
dictio = {k: v for k, v in tab}
print(dictio)






list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
fusion = {state: full_name for state, full_name in zip(list1, list2)}
print(fusion)







vowel_dict = {v: 0 for v in 'aeiou'}
print(vowel_dict)






alphabet = {i - 64: chr(i) for i in range(65, 91)}
print(alphabet)





phrase = "awesome sauce"
vowels_count = {v: phrase.count(v) for v in 'aeiou'}
print(vowels_count)