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
    a.lower()
    a.replace(" ", "")
    reverse_a = a[::-1]
    if a == reverse_a:
        return True
    else:
        return False

print(is_palindrome('testing'))
print(is_palindrome('tacocat'))
print(is_palindrome('hannah'))
print(is_palindrome('robert'))




def frequency(tab, value):
    count = 0
    for i in tab:
        if i == value:
            count +=1
    return count

print(frequency([1,2,3,4,4,4], 4))
print(frequency([True, False, True, True], False))




def flip_case(string, letter):
    result = ""
    for char in string:
        if char.lower() == letter.lower():
            result += char.swapcase()
        else:
            result += char
    return result

print(flip_case("Hardy har har", "h"))




def multiply_even_numbers(tab):
    product = 1
    even_numbers = []
    for i in tab:
        if i % 2 == 0:
            even_numbers.append(i)
    for i in even_numbers:
        product *= i
    return(product)

print(multiply_even_numbers([2,3,4,5,6]))




def mode(tab):
    count = {}
    for i in tab:
        count[i] = count.get(i, 0) + 1
    maxi = max(count.values())
    for number, values in count.items():
        if values == maxi:
            return number

print(mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]))




def capitalize(string):
    new_string = string.capitalize()
    return new_string

print(capitalize("tim"))
print(capitalize("tim"))




def compact(tab):
    result = []
    for i in tab:
        if i:
            result.append(i)
    return result

print(compact([0,1,2,"",[], False, {}, None, "All done"]))





def partition()