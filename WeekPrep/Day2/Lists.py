#Exercise : List #1

list = [1,2,3,4]

for i in list:
    print(i)

for i in list:
    print(i*20)



list = ["Elie", "Tim","Matt"]
list2 = []

for name in list:
    for letter in name:
        if letter.isupper():
            list2.append(letter)

print(list2)



list = [1,2,3,4,5,6]
list2 = []

for values in list:
    if values % 2 == 0:
        list2.append(values)

print(list2)



list1 = [1,2,3,4]
list2 = [3,4,5,6]
intersection = []

index_max1 = len(list1) - 1 
index_max2 = len(list2) - 1 

for idx, values in enumerate(list1):
    if idx == index_max1 // 2:
        intersection.append(values)

for idx, values in enumerate(list2):
    if idx == index_max2 // 2:
        intersection.append(values)

print(intersection)



list1 = ["Elie", "Tim", "Matt"]
list2 = []

for name in list1:
    name_reverse = name[::-1].lower()
    list2.append(name_reverse)

print(list2)



a = "first"
b = "third"
similarities = []

for letters in a:
    for letter in b:
        if letters == letter:
            similarities.append(letter)

print(similarities)



a = "amazing"
vowels = ["a","e","i","o","u","y"]
result = []

for letters in a:
    for letter in vowels:
        if letters == letter:
            break
    else:
        result.append(letters)

print(result)




list = []

for i in range(0,3):
    list.append(i)
    
new_list = []

for i in range(3):
    new_list.append(list)

print(new_list)





list = []

for i in range(0,10):
    list.append(i)

new_list = []

for i in range(10):
    new_list.append(list)

print(new_list)