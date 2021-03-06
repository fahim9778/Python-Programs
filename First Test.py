# All exercises from "Python Crash Course" book

"""
# Exercise 2-1
name = "Eric hudson"
print("Hello " + name + ", are you afraid of Python?")

print(name.upper())
print(name.lower())
print(name.title())

famous_person = "Albert Einstein "
quote = "\"A person who never made a mistake never tried anything new\""
print(famous_person.rstrip() + " once said, " + quote);


# Exercise 2-2
print(5+3)
print(11-3)
print(2*4)
print(56/7)

favorite_number = 3
message = "This is the " + str(favorite_number) + "rd time you're asking the same question"
print(message.title())



# Exercise 3-1-2
friends = ['Tarik', 'Tahmid', 'Abir']
print("Hey, " + friends[0]+ " welcome.")

vehicles = ['Honda', 'Ferrari', 'BMW']
print("I'd like to have a "+ vehicles[-1] + " Car")
print("I'd also like to have a "+ vehicles[-2] + " Car")
print("I'd like to have a "+ vehicles[-3] + " Motorbike")



# Exercise 3-4 : Guest list

guest_list = ['Tarik', 'Habib', 'Abir Azad']  # adding guest names;
print(guest_list)
print(guest_list[0] + ", you're cordially invited to this Grand Dinner.")
print(guest_list[1] + ", you're cordially invited to this Grand Dinner.")
print(guest_list[2] + ", you're cordially invited to this Grand Dinner.")

# Exercise 3-5 : Replacing guest
print(guest_list[0] + ", sorry to hear that you can't make it tonight.")
guest_list[1] = 'Shoummo'  # Changing guest 2
print(guest_list)
print(guest_list[1] + ", you're cordially invited to this Grand Dinner.")

# Exercise 3-6 : More guests
print("Hey everyone, We've got a dig Dinner table. So let's invite more! ")
guest_list.insert(0, 'Lami')    # adding a new at the beginning
guest_list.insert(2, 'Fahim')   # adding a new at the 3rd position
guest_list.append('Tahmid')     # adding a new at the last
print(guest_list)

# Exercise 3-7 : Shrinking guests
print("Sorry Everyone, The dinner won't come in time. So I must invite only  of you at at time. Apologies.")
popped_guest = guest_list.pop()    # removing an item from the last index using pop()
print(guest_list)
print("Sorry " + popped_guest+ ", you can't come today because of sudden table shortage.")
del guest_list[2:]  # removing multiple items (from 3rd to last) from the list using ranged del
print(guest_list)
print(guest_list[0] + ", you're still cordially invited to this Grand Dinner.")
print(guest_list[1] + ", you're still cordially invited to this Grand Dinner.")
del guest_list  # removing all guests from the list
print(guest_list)



# Exercise 3-8 : Seeing the world
place_to_visit = ['Singapore', 'America', 'Sweden', 'Paris', 'Saudi Arabia']
print(place_to_visit)   # Normal printing
print(sorted(place_to_visit))   # Printing with temporary sorting order
print(sorted(place_to_visit, reverse=True))     # Printing with temporary reverse-sorting order
place_to_visit.reverse()    # Actual Permanent reverse of input order, not sorted.
print(place_to_visit)
place_to_visit.sort()   # Actual Permanent Alphabetical sorting order
print(place_to_visit)
place_to_visit.sort(reverse=True)   # same as places_to_visit.reverse()
print(place_to_visit)


# Exercise 4-1 : Pizzas
pizzas = ['Mozzarella', 'Pepperoni', 'BBQ']     # pizza list
for pizza in pizzas:    # using for loops to iterate every pizza name
    print("I love " + pizza + " pizza!")
print("I really love pizza.")

# Exercise 4-2: Animals
animals = ['Lion', 'Tiger', 'Wolf']
for animal in animals:
    print("Look! There's " + animal + " over the top")
print("All of them are gonna hunt us down")



# Exercise 4-3: Counting Numbers
numbers_to_20 = []  # empty list
for number in range(1, 21):     # ranging numbers from 1 to 20 using for loop
    numbers_to_20.append(number)    # appending after the empty list
print(numbers_to_20)    # printing the list



# Exercise 4-4: Printing the millions
numbers_upto_million = []
for number_million in range(1,1_000_001):
    numbers_upto_million.append(number_million)
#print(numbers_upto_million)
print(min(numbers_upto_million))    # printing the minimum number
print(max(numbers_upto_million))    # printing the maximum number
print(sum(numbers_upto_million))    # printing the sum of one million


# Exercise 4-7: Threes
division_By_3 = []
for number_3 in range(1, 21):   # numbers ranging from 1 to 2
    if number_3 % 3 == 0:   # Checking if the number is divisible by 3
        division_By_3.append(number_3)  # if yes, then append to the list
print(division_By_3)

# Exercise 4-9: Cubes in comprehension
cubes_compre = [number**3 for number in range(1, 11)]
print(cubes_compre)


# Exercise 4-10: Slices
slices = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
print(slices[:3])   # printing first three items
print(slices[2:5])  # printing  middle three items
print(slices[-3:])  # printing last three times, reverse iterating


# Uncomment exercise 4-1: Pizza
friends_pizza = pizzas[:]
pizzas.append('Spanish')
pizzas.append('Thin Crust Salsa')
# print("My favorite pizzas are : " + str(pizzas))    # Bad type of iteration
# Good type of iteration is
for pizza in pizzas:
    print("My favorite pizza is : " + pizza)
# print("My friend's favorites are : " + str(friends_pizza))   # Bad type of iteration
for friend_pizza in pizzas:
    print("My friend's favorite pizza is : " + friend_pizza)


# Exercises from 'Python Crash Course, 2nd Edition' starts here
# Exercise 4-13: Buffet
buffet_menu = ('rice', 'potato', 'chicken', 'vegetables', 'fish')
print("Original Buffet Menu :")
for food in buffet_menu:
    print(food)
# buffet_menu[1] = 'papaya'
# ERROR : 'tuple' object does not support item assignment
buffet_menu = ('rice', 'papaya', 'chicken', 'vegetables', 'lobster')
print("\nRevised Buffet Menu :")
for revised_food in buffet_menu:
    print(revised_food)

# Exercise 5-8. Hello Admin
userNames = ['admin', 'bob', 'charlie', 'diana', 'elena']
for username in userNames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")


# Exercise 5-9. No Users
userNames = []
if userNames:
    for username in userNames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")

else:
    print("We need to find some users!")

# Exercise 5-10: Checking Usernames
current_users = ['adam', 'bob', 'charlie', 'diana', 'elena']
new_users = ['pat', 'bob', 'sam', 'elena', 'tim']
for userName in new_users:
    if userName.lower() in current_users:
        print(f"Sorry, Username {userName.title()} is not available")
    else:
        print(f"Congrats, Username {userName.title()} is available.")

# Exercise 5-11: Ordinal Numbers
ordinal_numbers = range(1, 10)
for number in ordinal_numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")

# Exercise 6-1: Person
person = {
    'first_name': 'Sarah',
    'last_name': 'Patin',
    'age': 34,
    'city': 'Dakota'
}
print(person)

# Exercise 6-2: Favorite Numbers
favorite_numbers = {
    'Adam': 7,
    'Barbara': 10,
    'Charlie': 11,
    'Don': 17,
    'Elena': 7
}
print(favorite_numbers)

# Exercise 6-3: Five Programming Languages
programming_languages = {
    'C++': 'The First Language of Mine.',
    'C' : 'I didn\'t knew I\'d to come down.',
    'Java': 'The Second one, Lengthy but Okay.',
    'PHP': 'Loved it, Beautiful One.',
    'Python': 'Still Learning...'
}
for name, experience in programming_languages.items():
    print(f"Language name : {name}")
    print(f"My Experience : {experience}\n")

# Exercise 6-5: Rivers
rivers_and_countries = {
    'nile': 'egypt',
    'mississippi': 'america',
    'ganges': 'india',
    'amazon': 'brazil',
    'zambezi': 'zimbabwe'
}
for river, country in sorted(rivers_and_countries.items()):
    print(f"{river.title()} runs through {country.title()}")

print("\nRiver names are:")
for river in rivers_and_countries.keys():
    print(f"{river.title()}")

print("\nCountry names are:")
for country in rivers_and_countries.values():
    print(f"{country.title()}")

# Exercise 6-6: Polls
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
people_list = ['charlie', 'sarah', 'bob', 'peri', 'erin', 'phil']
for name in people_list:
    if name in favorite_languages.keys():
        print(f"Thanks, {name.title()} for taking the poll.")
    else:
        print(f"Hey {name.title()}, would you please take our poll?")

# Exercise 6-7: People
person1 = {
    'first_name': 'Sarah',
    'last_name': 'Patin',
    'age': 34,
    'city': 'Dakota'
}
person2 = {
    'first_name': 'John',
    'last_name': 'Carry',
    'age': 30,
    'city': 'New York'
}
person3 = {
    'first_name': 'Mary',
    'last_name': 'Daisy',
    'age': 35,
    'city': 'Carolina'
}

people = [person1, person2, person3]
for person in people:
    for key, value in person.items():
        print(f"{key} = {value}")
    print("...")

# Exercise 6-8: Pets:
# dictionaries for pets
pet1 = {
    'pet_name': 'pup',
    'animal_type': 'dog',
    'owner_name': 'mike'
}

pet2 = {
    'pet_name': 'mew',
    'animal_type': 'cat',
    'owner_name': 'sarah'
}
pet3 = {
    'pet_name': 'tweety',
    'animal_type': 'bird',
    'owner_name': 'caron'
}
pet4 = {
    'pet_name': 'ron',
    'animal_type': 'horse',
    'owner_name': 'charlie'
}
pet5 = {
    'pet_name': 'meep',
    'animal_type': 'sheep',
    'owner_name': 'dalia'
}

# storing all dictionaries in a list
pets = [pet1, pet2, pet3, pet4, pet5]

# traversing thorough each dictionaries items
for pet in pets:
    for key, value in pet.items():
        print(f"{key} = {value.title()}")
    print("...")

# Exercise 6-9. Favorite Places; 6-11. Cities; 6-12. Extensions are same as above (Exercise 6-8)
# Exercise 6-10 Favorite Numbers:
favorite_numbers = {
    'Adam': [7, 15, 11],
    'Barbara': [10],  # for making iterable type
    'Charlie': [11, 19, 2],
    'Don': [17, 20, 5, 25],
    'Elena': [7]  # for making iterable type
}
for person, numbers in favorite_numbers.items():
    print(f"\n{person}\'s favorite number(s) :")
    for number in numbers:
        print(f"{number}")
print("...")

# Exercise 7-1 Rental Car:
car_name = input("Enter a car name: ")
print(f"Let me see if I can find you a {car_name.title()}.")

# Exercise 7-2 Restaurant Seating:
number_of_people = input("How many people are in the guest list? ")
number_of_people = int(number_of_people)
if number_of_people > 8:
    print(f"Sorry, you've to wait for a table.")
else:
    print("Welcome to the table, sir.")

# Exercise 7-3 Multiples of Ten:
number = input("Enter a number: ")
number = int(number)
if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is NOT multiple of 10.")

# Exercise 7-4 Pizza Toppings:
active = True
while active:
    topping = input("Enter your favorite topping names: "
                    "Enter 'quit' to terminate prompt. :: ")
    if topping.lower() == 'quit':
        active = False
        # alternatively we can use 'break' to terminate the while loop.
    else:
        print(f"{topping.title()}")

# Exercise 7-5 Movie Tickets:
active = True
while active:
    age = input("Enter your age."
                "Enter 'quit' to terminate prompt. :: ")
    if age.lower() == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print("Free Entry!")
        elif 3 <= age <= 12:
            print("Entry Fee: $10")
        elif age > 12 :
            print("Entry Fee: $15")

# Exercise 7-6 is already done in 7-4, 7-5
# Exercise 7-7 : Not Gonna try :p

# Exercise 7-8 Deli:
sandwich_orders = ["Grilled Cheese Sandwich", "Fish Sandwich", "Fried Egg Sandwich",
                   "Ham Sandwich", "Ice Cream Sandwich", "Meat Ball Sandwich"]
finished_sandwiches = []
while sandwich_orders:
    currently_cooking = sandwich_orders.pop()
    print(f"Hold tight! Your {currently_cooking} is being prepared...")

    finished_sandwiches.append(currently_cooking)
    print(f"We made your {currently_cooking} sandwich. Grab NOW!\n")

print("Hello folks! today we made these sandwiches : ")
for sandwich in finished_sandwiches:
    print(f"{sandwich}")

# Exercise 7-9 No Pastrami:
sandwich_orders = ["Grilled Cheese Sandwich", "Pastrami", "Fish Sandwich",
                   "Fried Egg Sandwich", "Pastrami", "Ham Sandwich",
                   "Ice Cream Sandwich", "Pastrami", "Meat Ball Sandwich"]
print(f"Oh no! Deli has run out of Pastrami! :(\n")
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")

finished_sandwiches = sandwich_orders
print("Hello folks! today we made these sandwiches : ")
for sandwich in finished_sandwiches:
    print(f"{sandwich}")

# Exercise 7-10 Dream Vacation:
responses = {}
# Set a flag to indicate that polling is active.
polling_active = True
while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")
    # Store the response in the dictionary.
    responses[name] = response
    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to visit {response}.")
"""
