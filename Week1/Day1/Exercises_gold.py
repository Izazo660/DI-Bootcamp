#Exercise 1 : Hello World-I love Python

print(("Hello world\n" * 4) + ("I love python\n" * 4).strip())

#Exercise 2 : What is the Season ?

month = int(input("Enter a month number (1 to 12): "))

if 3 <= month <= 5:
    print("The season is Spring.")
elif 6 <= month <= 8:
    print("The season is Summer.")
elif 9 <= month <= 11:
    print("The season is Autumn.")
elif month == 12 or month == 1 or month == 2:
    print("The season is Winter.")
else:
    print("Invalid month! Please enter a number between 1 and 12.")