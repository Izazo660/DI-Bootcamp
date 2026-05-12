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





def partition(tab, callback):
    result_even = []
    result_odd = []
    for i in tab:
        if callback(i) == True:
            result_even.append(i)
        else:
            result_odd.append(i)
    final_result = []
    final_result.append(result_even)
    final_result.append(result_odd)
    return final_result

def is_even(num):
    return num % 2 == 0

print(partition([1,2,3,4], is_even))





def intersection(tab1, tab2):
    result = []
    for i in tab1:
        for j in tab2:
            if i == j:
                result.append(j)
    return result

print(intersection([1,2,3], [2,3,4]))






def run_once(function):
    has_run = False
    def inner(*args, **kwargs):
        nonlocal has_run
        if not has_run:
            has_run = True
            return function(*args, **kwargs)
        return None
    return inner

def add(a,b):
    return a + b

one_addition = run_once(add)

print(one_addition(2,2))
print(one_addition(2,2))
print(one_addition(12,200))

@run_once
def add(a, b):
    return a + b

print(add(2,2))
print(add(2,20))
print(add(12,20))




#Exercise 2 : Functions Exercises#2

def reversed_strings(string):
    reverse_string = string[::-1]
    return reverse_string

print(reversed_strings("world"))
print(reversed_strings("word"))





import math

def benefactor(tab, target):
    sum = 0
    for i in tab:
        sum += i
    total_count = len(tab) + 1
    required_donation = (target * total_count) - sum
    if required_donation <= 0:
        return "The average is already met."
    return math.ceil(required_donation)

donations_list = [14, 30, 5, 7, 9, 11, 15]

print(f"Next donation needed: {benefactor(donations_list, 92)}")
print(f"Next donation needed: {benefactor(donations_list, 2)}")




def sequence(begin, end, step):
    return sum(range(begin, end + 1, step))

print(sequence(2,2,2))
print(sequence(2,6,2))
print(sequence(1,5,1))
print(sequence(1,5,3))





def max_diff(tab):
    if len(tab) <= 1:
        return 0
    else:
        return max(tab) - min(tab)

print(max_diff([1, 2, 3, 4]))
print(max_diff([1, 2, 3, -4]))




def countSmileys(a):
    count = 0
    for i in a:
        if len(i) == 2:
            if i[0] in ":;" and i[1] in ")D":
                count +=1
        elif len(i) == 3:
            if i[0] in ":;" and i[1] in "-~" and i[2] in ")D":
                count +=1
    return count

print(countSmileys([':)', ';(', ';}', ':-D']))
print(countSmileys([';D', ':-(', ':-)', ';~)']))
print(countSmileys([';]', ':[', ';*', ':$', ';-D']))




def sentences(paragraph):
    count = 0
    for i in paragraph:
        if i == "." or i == "?" or i == "!":
            count += 1
    return count

print(sentences("My name is Ismael. I am 18 years old. I live in France ! What about ?"))
print(sentences("Hello"))





def race(v1, v2, g):
    if v1 >= v2:
        return None
    closing_speed = v2-v1
    total_seconds = (g * 3600) // closing_speed
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return [hours, minutes, seconds]

print(race(720, 850, 70))
print(race(80, 91, 37))





def rotation(string1, string2):
    if len(string1) != len(string2):
        return -1
    elif string1 == string2:
        return 0
    combined = string2 + string2
    idx = combined.find(string1)
    return idx

print(rotation("coffee", "eecoff"))
print(rotation("eecoff", "coffee"))
print(rotation("moose", "Moose"))
print(rotation("isn't", "'tisn"))
print(rotation("Esham", "Esham"))
print(rotation("dog", "god"))