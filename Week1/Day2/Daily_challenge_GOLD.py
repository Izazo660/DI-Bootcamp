from datetime import datetime

birthdate_input = input("Enter your birthdate (DD/MM/YYYY): ").strip()

birthdate = datetime.strptime(birthdate_input, "%d/%m/%m/%Y")

current_year = 2026
age = current_year - birthdate.year

num_candles = int(str(age)[-1])

year = birthdate.year
is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

num_cakes = 2 if is_leap_year else 1

candles_str = "i" * num_candles
top_cake = f"{candles_str}".center(11, "_")

cake_ascii = f"""
       {top_cake}
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
"""

print(f"\nYou are {age} years old. Here is your cake:")
for _ in range(num_cakes):
    print(cake_ascii)