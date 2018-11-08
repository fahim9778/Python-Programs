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

"""
# Exercise 4-13: Buffet
buffet = ('rice', 'chicken', 'steak', 'vegetable', 'curry')     # Tuple created
print("Original Menu :")
for food in buffet:
    print(food.title())     # Iterating through tuple

# buffet[0] = 'noodles'     # This creates problem, No assignment in tuple
buffet = ('noodles', 'chicken', 'steak', 'vegetable', 'pickles')    # Re-written Tuples
print("\nModified Menu :")
for food in buffet:
    print(food.title())     # Iterating through tuple