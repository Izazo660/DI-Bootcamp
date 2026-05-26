#Exercise 1: Currencies

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    #Your code starts HERE

    def __str__(self):
        suffix = "s" if self.amount > 1 else ""
        return f"{self.amount} {self.currency}{suffix}"

    def __repr__(self):
        suffix = "s" if self.amount > 1 else ""
        return f"'{self.amount} {self.currency}{suffix}'"

    def __int__(self):
        return self.amount

    def __add__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return self.amount + other.amount
        elif isinstance(other, (int, float)):
            return self.amount + other
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
        elif isinstance(other, (int, float)):
            self.amount += other
        else:
            return NotImplemented
        return self

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

#the comment is the expected output
print(c1)
# '5 dollars'

print(int(c1))
# 5

print(repr(c1))
# '5 dollars'

print(c1 + 5)
# 10

print(c1 + c2)
# 15

print(c1) 
# 5 dollars

c1 += 5
print(c1)
# 10 dollars

c1 += c2
print(c1)
# 20 dollars

#print(c1 + c3)
# TypeError: Cannot add between Currency type <dollar> and <shekel>
#comment the print above before you run the file for next exercises (since the error will crash your file)


#Exercise 2: Import
def sum_and_print(num1, num2):
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is: {result}")

#from Exercises.py import sum_and_print

# Call the imported function
sum_and_print(12, 18)  # Output: The sum of 12 and 18 is: 30



#Exercise 3: String module

import string
import random

def generate_random_string(length=5):
    all_letters = string.ascii_letters
    random_chars = [random.choice(all_letters) for _ in range(length)]
    return "".join(random_chars)

print("Generated string:", generate_random_string(5))



#Exercise 4: Current Date

from datetime import datetime

def display_current_date():
    today = datetime.now().date()
    print("Today's Date:", today.strftime("%d-%m-%Y"))

display_current_date()



#Exercise 5: Amount of time left until January 1st

from datetime import datetime

def time_until_new_year():
    now = datetime.now()
    next_year = now.year + 1
    new_year_target = datetime(year=next_year, month=1, day=1, hour=0, minute=0, second=0)
    time_left = new_year_target - now
    print(f"Time remaining until January 1st, {next_year}:")
    print(time_left)

time_until_new_year()




#Exercise 6: Birthday and minutes

from datetime import datetime

def minutes_lived(birthday_str):
    """Expects string format format: 'YYYY-MM-DD'"""
    try:
        birth_date = datetime.strptime(birthday_str, "%d-%m-%Y")
        now = datetime.now()
        life_delta = now - birth_date
        total_minutes = int(life_delta.total_seconds() / 60)
        print(f"You have lived approximately {total_minutes:,} minutes in your life!")
    except ValueError:
        print("Incorrect date format! Please use 'DD-MM-YYYY'.")

minutes_lived("21-05-2007")




#Exercise 7: Faker Module

from faker import Faker

users = []
fake = Faker()

def add_fake_users(number_of_users):
    for _ in range(number_of_users):
        user_profile = {
            "name": fake.name(),
            "address": fake.address().replace("\n", ", "),
            "language_code": fake.language_code()
        }
        users.append(user_profile)

add_fake_users(3)

import pprint
pprint.pprint(users)