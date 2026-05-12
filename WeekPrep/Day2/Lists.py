numbers = [1, 2, 3, 4]
[print(val) for val in numbers]





times_twenty = [val * 20 for val in numbers]
print(times_twenty)




names = ["Elie", "Tim", "Matt"]
first_letters = [name[0] for name in names]
print(first_letters)




evens_list = [1, 2, 3, 4, 5, 6]
evens = [val for val in evens_list if val % 2 == 0]
print(evens)




l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 6]
intersection = [val for val in l1 if val in l2]
print(intersection)





reversed_names = [name[::-1].lower() for name in names]
print(reversed_names)







s1 = "first"
s2 = "third"
similarities = [char for char in "i r t" if char in s1 and char in s2]
similarities = list({char for char in s1 if char in s2})
print(similarities)







div_by_12 = [n for n in range(1, 101) if n % 12 == 0]
print(div_by_12)






word = "amazing"
no_vowels = [char for char in word if char not in "aeiou"]
print(no_vowels)






nested_3 = [[val for val in range(3)] for _ in range(3)]
print(nested_3)







nested_10 = [[val for val in range(10)] for _ in range(10)]
print(nested_10)