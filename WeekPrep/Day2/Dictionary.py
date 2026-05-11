#Exercise 1 : Dictionary Exercises

tab = [("name", "Elie"), ("job", "Instructor")]

dictio = dict(tab)

print(dictio)





list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

fusion = dict(zip(list1, list2))

print(fusion)





vowel = ["a", "e", "i", "o", "u"]
values = [0] * len(vowel)

dictionary = dict(zip(vowel, values))

print(dictionary)




letters = []
values = []

for i in range(65,91):
    letters.append(chr(i))
    values.append(i-64)

alphabet = dict(zip(letters, values))

print(alphabet)




vowels_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for i in "awesome sauce":
    if i in vowels_count:
        vowels_count[i] +=1

print(vowels_count)