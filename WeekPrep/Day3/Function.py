#Exercise 1 : Functions Exercises #1

def difference(a,b):
    return a - b

print(difference(2,2))
print(difference(0,2))



def print_day(a):
    if a >= 1 and a <= 7:
        if a == 1:
            return "Sunday"
        if a == 2:
            return "Monday"
        if a == 3:
            return "Tuesday"
        if a == 4:
            return "Wednesday"
        if a == 5:
            return "Thursday"
        if a == 6:
            return "Friday"
        if a == 7:
            return "Saturday"
    else:
        return None

print(print_day(4))
print(print_day(41))




def last_element(list):
    if list == []:
        return None
    else:
        return list[-1]

print(last_element([1,2,3,4]))
print(last_element([]))




def number_compare(a,b):
    if a > b:
        return "First is greater."
    elif a < b:
        return "Second is greater."
    else:
        return "Numbers are equal."

print(number_compare(1,1))
print(number_compare(1,2))
print(number_compare(2,1))




def single_letter_count(word,letter):
    count = 0
    for i in word:
        if i == letter:
            count += 1
    return count

print(single_letter_count('amazing','A'))
print(single_letter_count('amazing','a'))



def multiple_letter_count(a):
    count = {}
    for letter in a:
        if letter in count:
            count[letter] +=1
        else:
            count[letter] = 1
    return count

print(multiple_letter_count("hello"))
print(multiple_letter_count("person"))




def list_manipulation(list,command,location,value):
    if command == "remove" and location == "end":
        return list.pop(-1)
    elif command == "remove" and location == "beginning":
        return list.pop(0)
    elif command == "add" and location == "beginning":
        list.insert(0, value)
        return list
    elif command == "add" and location == "end":
        list.append(value)
        return list


print(list_manipulation([1,2,3], "remove", "end", 0 ))
print(list_manipulation([1,2,3], "remove", "beginning", 0))
print(list_manipulation([1,2,3], "add", "beginning", 20))
print(list_manipulation([1,2,3], "add", "end", 30))

def is_palindrome(a):
    tab = list(a)
    reverse_tab = tab.reverse()
    word = []
    for i in tab:
        for j in tab :
            if i == j:
                word.append(j)
    return word

print(is_palindrome('testing'))
