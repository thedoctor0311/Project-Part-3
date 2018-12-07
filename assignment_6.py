# 6-1. Person: Use a dictionary to store information about a person you know .
# Store their first name, last name, age, and the city in which they live .
# You should have keys such as first_name, last_name, age, and city .
# Print each piece of information stored in your dictionary .
person_0 = {
    'first_name': 'jio',
    'last_name': 'torres',
    'age': 17,
    'city': 'aurora',
}
print(person_0['first_name'])
print(person_0['last_name'])
print(person_0['age'])
print(person_0['city'])

# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers .
# Think of five names, and use them as keys in your dictionary .
# Think of a favorite number for each person, and store each as a value in your dictionary .
# Print each person’s name and their favorite number.
# For even more fun, poll a few friends and get some actual data for your program .

favorite_numbers = {
    'madu': ' 5',
    'josh': ' 6',
    'tony': ' 4',
    'mike': ' 2',
    'kevin': ' 8',
}

print("Madu's favorite_numbers is" +
      favorite_numbers['madu'].title() +
      ".")

print("Josh's favorite_numbers is" +
      favorite_numbers['josh'].title() +
      ".")

print("Tony's favorite_numbers is" +
      favorite_numbers['tony'].title() +
      ".")

print("Mike's favorite_numbers is" +
      favorite_numbers['mike'].title() +
      ".")

print("Kevin's favorite_numbers is" +
      favorite_numbers['kevin'].title() +
      ".")

# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary .
# However, to avoid confusion, let’s call it a glossary .
glossary = {
    'range': ' range between series of numbers',
    'list': ' group of items in a set order',
    'loop': 'rub through list',
    'dictionary': 'key value pairs',
    'string': 'series of characters',
}
word = 'range'
print("\n" + word.title() + ": " + glossary[word])

word = 'list'
print("\n" + word.title() + ": " + glossary[word])

word = 'loop'
print("\n" + word.title() + ": " + glossary[word])

word = 'dictionary'
print("\n" + word.title() + ": " + glossary[word])

word = 'string'
print("\n" + word.title() + ": " + glossary[word])

# 6-4. Glossary 2: Now that you know how to loop through a dictionary,
# clean up the code from Exercise 6-3 (page 102) by replacing your series
# of print statements with a loop that runs through the dictionary’s keys and values .
# When you’re sure that your loop works, add five more Python terms to your glossary .
# When you run your program again, these new words and meanings should automatically be included in the output .
glossary = {
    'range': ' range between series of numbers',
    'list': ' group of items in a set order',
    'loop': 'rub through list',
    'dictionary': 'key value pairs',
    'string': 'series of characters',
    'comment': 'side notes in a program that the Python ignores.',
    'key': 'first item in a dictionary.',
    'value': 'item associated with a key.',
    'conditional test': 'comparison between two values.',
    'float': 'numerical value with a decimal.',
    }

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)

# 6-6. Polling: Use the code in favorite_languages.py (page 104).
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
print("\n")

coders = ['jen', 'sarah', 'edward', 'phil', 'mike', 'bobby']
for coder in coders:
    if coder in favorite_languages.keys():
        print("Thank you for taking the poll, " + coder.title() + "!")
    else:
        print(coder.title() + ", what's your favorite programming language?")

# 6-8. Pets: Make several dictionaries, where the name of each dictionary is the name of a pet .
# In each dictionary, include the kind of animal and the owner’s name .
# Store these dictionaries in a list called pets .
# Next, loop through your list and as you do print everything you know about each pet .
pets = []
pet = {
    'animal type': 'shih tzu',
    'name': 'cookie',
    'owner': 'rick',
}
pets.append(pet)

pet = {
    'animal type': 'doberman',
    'name': 'oreo',
    'owner': 'bobby',
}
pets.append(pet)

pet = {
    'animal type': 'chow chow',
    'name': 'fluff',
    'owner': 'jim',
}
pets.append(pet)

for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))

# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102)
# so each person can have more than one favorite number .
# Then print each person’s name along with their favorite numbers .
favorite_numbers = {
    'mhud': [3, 18],
    'tony': [6, 12],
    'josh': [5, 15],
    }

for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + " likes the following numbers:")
    for number in numbers:
        print("  " + str(number))

# 6-12. Extensions: We’re now working with examples that are complex enough
# that they can be extended in any number of ways .
# Use one of the example programs from this chapter,
# and extend it by adding new keys and values, changing the context of the
# program or improving the formatting of the output .
person = {
    'first_name': 'jio',
    'last_name': 'torres',
    'age': 17,
    'city': 'aurora',
    'first_name digit': 3,
    'last_name digit': 6,
}

for name, numbers in person.items():
    print("\n" + name.title() + " How many letters in each word:")

# 7-1. Rental Car: Write a program that asks the user what kind of rental car they would like .
# Print a message about that car, such as “Let me see if I can find you a Subaru.
car = "What kind of car would you like? "
car = 'Subaru'
print("Let me see if I can find you a " + car.title() + ".")

# 7-2. Restaurant Seating: Write a program that asks the user how many people are in their dinner group .
# If the answer is more than eight, print a message saying they’ll have to wait for a table .
# Otherwise, report that their table is ready .
party_size = input("How many people are in your dinner party tonight? ")
party_size = int(party_size)

if party_size > 8:
    print("I'm sorry, you'll have to wait for a table.")
else:
    print("Your table is ready.")

# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not .
number = input("Give me a number, please: ")
number = int(number)

if number % 10 == 0:
    print(str(number) + " is a multiple of 10.")
else:
    print(str(number) + " is not a multiple of 10.")

# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of pizza
# toppings until they enter a 'quit' value.
# As they enter each topping, print a message saying you’ll add that topping to their pizza .
prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print("  I'll add " + topping + " to your pizza.")
    else:
        break

# 7-8 Make a list called sandwich_orders and fill it with the names of various sandwiches.
# Then make an empty list called finished_sandwiches.
# Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich.
# As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made.'''
sandwich_orders = ['chicken', 'bbq buffalo', 'mac cheese', 'big steak']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")
'''7-10 Write a program that polls users about their dream vacation. Write a prompt similar to 
If you could visit one place in the world, where would you go? 
Include a block of code that prints the results of the poll'''
name_prompt = "\nWhat's your name? "
place_prompt = "If you could visit one place in the world, where would it be? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "

# Responses will be stored in the form {name: place}.
responses = {}

while True:
    # Ask the user where they'd like to go.
    name = input(name_prompt)
    place = input(place_prompt)

    # Store the response.
    responses[name] = place

    # Ask if there's anyone else responding.
    repeat = input(continue_prompt)
    if repeat != 'yes':
        break

# Show results of the survey.
print("\n--- Results ---")
for name, place in responses.items():
    print(name.title() + " would like to visit " + place.title() + ".")
'''8-1 Write a function called display_message() that prints one sentence telling everyone 
what you are learning about in this chapter. Call the function, and make sure the message displays correctly'''
def display_message():
    """Display a message about what I'm learning."""
    msg = "I'm learning to store code in functions."
    print(msg)

display_message()

'''8-2 Write a function called favorite_book() that accepts one parameter, title. 
The function should print a message, such as One of my favorite books is Alice in Wonderland. 
Call the function, making sure to include a book title as an argument in the function call'''
def favorite_book(title):
    """Display a message about someone's favorite book."""
    print(title + " is one of my favorite books.")

favorite_book('The Abstract Wild')

'''8-4 Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
 Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message'''
def make_shirt(size='large', message='I love Python!'):
    """Summarize the shirt that's going to be made."""
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Programmers are loopy.')

#8-6 Write a function called city_country() that takes in the name of a city and its country. 
#The function should return a string formatted like this:
#“Santiago, Chile”
#Call your function with at least three city-country pairs, and print the value that’s returned.
def city_country(city, country):
    """Return a string like 'Santiago, Chile'."""
    return(city.title() + ", " + country.title())

city = city_country('San Juan', 'Puerto Rico')
print(city)

city = city_country('Talca', 'Chile')
print(city)

city = city_country('Shanghai', 'China')
print(city)

# 8-8 Start with your program from Exercise 8-7. Write a while loop that allows users
# to enter an album’s artist and title. Once you have that information, call make_album() 
# with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.


def make_album(artist, title, tracks=0):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
    }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict


# Prepare the prompts.
title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who's the artist? "

# Let the user know how to quit.
print("Enter 'quit' at any time to stop.")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break

    artist = input(artist_prompt)
    if artist == 'quit':
        break

    album = make_album(artist, title)
    print(album)

print("\nThanks for responding!")

'''8-10 Start with a copy of your program from Exercise 8-9. 
Write a function called make_great() that modifies the list of magicians by adding 
the phrase the Great to each magician’s name. Call show_magicians() 
to see that the list has actually been modified.'''
def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """Add 'the Great!' to each magician's name."""
    # Build a new list to hold the great musicians.
    great_magicians = []

    # Make each magician great, and add it to great_magicians.
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    # Add the great magicians back into magicians.
    for great_magician in great_magicians:
        magicians.append(great_magician)

magicians = ['Harry Houdini', 'David Blaine', 'Teller']
show_magicians(magicians)

print("\n")
make_great(magicians)
show_magicians(magicians)

'''8-12 Write a function that accepts a list of items a person wants on a sandwich. 
The function should have one parameter that collects as many items as the function call provides, 
and it should print a summary of the sandiwch that is being ordered. Call the function three items,
 using a different number of arguments each time'''
def make_sandwich(*items):
    """Make a sandwich with the given items."""
    print("\nI'll make you a great sandwich:")
    for item in items:
        print("  ...adding " + item + " to your sandwich.")
    print("Your sandwich is ready!")

make_sandwich('tuna', 'swiss cheese', 'lettuce', 'cucumbers')
make_sandwich('beef', 'ham', 'honey mustard')
make_sandwich('peanut butter', 'banana slices')

'''8-14 Write a function that stores information about a car in a dictionary. 
the function should always receive a manufacturer and a model name. 
It should then accept an arbitrary number of keyword arguments. 
Call the function with the required information and two other name-value pairs, such as a color or an optional feature.
Your function should work for a call like this one:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that’s returned to make sure all the information was stored correctly.'''
def make_car(manufacturer, model, **options):
    """Make a dictionary representing a car."""
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
        }
    for option, value in options.items():
        car_dict[option] = value

    return car_dict

my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_outback)

my_accord = make_car('honda', 'accord', year=1991, color='white',
        headlights='popup')
print(my_accord)

'''8-15 Put the functions for the example printing_models.py in a separate file called printing_functions.py. 
Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.
Note: The text refers to print_models.py, but it should say printing_models.py.
printing_functions.py:'''
"""Functions related to printing 3d models."""


def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until there are none left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simulate creating a 3d print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

