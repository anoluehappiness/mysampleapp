# printing my first program
"""print ("Anolue Ijeoma")
print (" o----")
print ("  ||||")"""

# printing my first variable program
"""print = 10
rating = 4.9
name ="Ijeoma"
is_published = True
print (price)"""

#

# my variable exercise
"""name = "John Smith"
age = "20"
a_new_patient = True"""


# this is a concatenation
"""name = input ("what is your name?  ")
print ("Hi "  + name)"""


# the use of input() to concate two variables
"""name = input ("what is your name? ")
favourite_colour = input ("what is your favourite colour? ")
print (name + " likes " + favourite_colour)"""


# exercise o input()
"""birth_year = input("Birth year: ")
print (type(birth_year))
age = 2022 - int(birth_year)
print (type(age))
print(age)"""

# exercise on input()
"""pounds = int(input("what is your weight in pounds?  "))
#remember 1pound = 0.454kg
kg = pounds * 0.454
print(str(kg) + " " + "Kg")"""

# strings
"""course = "Pyton for Beginners"
print(course[0:3])"""

# the use of formatted strings
"""first = 'John'
last = 'Smith'
message = first + ' [' + last +  '] is a coder'
msg = f'{first} [{last}] is a coder'
print(msg)"""


# the use of replace() on strings
"""course = Pyton for beginners"
print(course .replace("P", "J"))"""


# the use of ... in operation in a strings
"""course =" Pyton for beginners"
print("Pyton" in course)"""



# the use of absolute () in solving integers and float
"""x = 2.9  
print(abs(x))"""


# the use of 'if' statement
"""house_price = 1000000
has_good_credit = input("Have good Credit, Y/N?: ")
if has_good_credit == 'Y':
    down_payment = house_price * 0.1
else:
    down_payment = house_price * 0.2
print('$' + str(down_payment))"""


# the use of logical operation"and","or",not"
"""has_high_income = False
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan")"""



# the use of comparism statements
"""name = "Anolue Happiness "

if len(name) < 3:
    print("name is at least 3 characters")
elif len(name) > 50:
    print("name can be maximum of 50 characters")
else:
    print("name looks good!")"""
# this is a statement

# Revision
"""weight =int(input("weight: "))
unit = input("(l)bs or (k)g: ")
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted}kg")
else:
    converted = weight/0.45
    print(f"You are {converted}pounds")"""


# the use of while loop
"""i = 1
while i <= 5:
     print("*" * i)
    i = i + 1
print("Done")"""



# the use of while loop
"""secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess:"))
))))    guess_count  += 1
    if guess ==secret_number:
        print("You won!")
        break
else:
    print("You failed")"""
# this is a comment

# the use of while loops
"""command = ""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
              print("car is already started!")
        else:
            started = True
        print("car started...")
    elif command == "stop":
     if not started:
       print("car is already stopped!")
else:
    started = false"""

# th use of for loops
"""for item in "python":
    print(item)

    for item in range(5,10 ):
        print(item)"""
# this is a comment

# prices = [10, 20, 30]
# the use of for loops
"""total = 0
for item in prices:
     total += item
print(f"Total: {total}")"""
# this is a comment

# the use of nested loops
"""for x in range(5):
          print(f"{x}, {y}")"""
# this is a comment


# the use of nested loops
"""numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
     print("x" * x_count)"""
# this is a comment


# numbers = [5, 2, 5, 2, 2]
#  for x_count in numbers:
# output = ""
# for count in range(x_count):
#    print(output)

# numbers = [2, 4, 7, 9, 7, 5, 8]
# uniques = []
# for number in numbers:
# if numbers not in uniques:
# uniques.append(number)
# printSS

# the use of fo loops
# prices = [10, 20, 30]
# total = 0
# for price in prices:
# print(total)

# nested loops
# for x in range (4):
# for y in range(3):
# print(f"({x}, {y}) ")


# numbers = [5, 2, 5, 2, 2]
# for x_count in numbers:
# output = " "
# for count in range(x_count):
# output += "x"
# print(output)


# list
# names = ["John", "Bob", "Mosh", "sarah", "mary"]
# names[0] = "charles"
# print(names )


# exercise on list
# numbers = [5, 6, 8, 7, 9]
# maxi = numbers[0]
# for number in numbers:
# if number > maxi:
# maxi = number
# print(maxi)

# 2D lists

# matrix = [
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]
# ]
# matrix[0][1] = 20
# print(matrix[0][1])



 
