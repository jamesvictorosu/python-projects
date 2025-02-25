# JVM Get Age program
# This program will prompt a user for their name and birth year, then output how old they will be this year
from datetime import date

current_date = date.today()
# Get the current year
current_year = current_date.year

# Receiving Input - User name
name = input("What is your name? ")

# Validate name input
while name == "":
    print("You did not enter your name.")
    name = input("What is your name? ")

# Greet the user
# option 1: using concatenation
# print("Hello " + name + "!")
# option 2: formatted string - cleaner method
print(f"Hello {name}!")

# Receive and validate birth year input
# input() by default returns a string, so convert to integer to use in age variable calculation
while True:
    try:
        birth_year = int(input("Enter your birth year: "))
        if birth_year > current_year:
            print("Birth year cannot be in the future. Please try again.")
        else:
            break
    except ValueError:
        print("Please enter a valid year.")

# Calculate and display age
age = current_year - birth_year
# option 1: concatenation option - longer and more complex
# print(name + ","  " you will be " + str(age) + " years old this year!")
# option 2: formatted string - cleaner and more concise
print(f"{name}, you will be {age} years old this year!")
