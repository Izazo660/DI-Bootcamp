#Exercise 1: Hello World

print("Hello World\n" * 3) 

#Exercise 2: Some Math

result = (99**3)*8
print(result)

#Exercise 3: What is the output?

5 < 3 #False
3 == 3 #True
3 == "3" #False
#"3" > 3 #False
"Hello" == "hello" #False

#Exercise 4: Your computer brand

computer_brand = input("Your computer brand name : ")
print(f"I have a {computer_brand} computer.")

#Exercise 5 : Your information

name = "Erridaoui Ismael"
age = 18
shoe_size = 41
info = f"My name is {name}, I'm {age} years old and my shoe size is {shoe_size}."
print(info)

#Exercise 6: A & B

a = 8
b = 6
if a > b:
    print("Hello World")

#Exercise 7: Odd or Even

number = input("Give me a number : ")

if int(number) % 2 == 0:
    print("Even")
else:
    print("Odd")

#Exercise 8: What’s your name?

name = input("What is your name ? ")
my_name = "Ismael"

if name == "Ismael":
    print("OMG WE HAVE THE SAME NAME LETS BE FRIENDS")
else:
    print("We don't have the same name sadly..")

#Exercise 9: Tall enough to ride a roller coaster

height = input("What is your height ? (in centimers) ")

if int(height) > 145:
    print("You are tall enough to ride !")
else:
    print("You need to grow more to ride.")