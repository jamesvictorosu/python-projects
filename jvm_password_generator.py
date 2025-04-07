# JVM Password Generator program
# This program generates a random password and performs exception handling
import string
import random

# Ask user for desired password length
while True:
    try:
        length = int(
            input("Enter a number for password length (MIN 8, MAX 40): "))
        if length <= 0:
            raise ValueError("Length must be a positive number.")
        if length < 8:
            raise ValueError("Password length must be at least 8.")
        if length > 40:
            raise ValueError("Password length must not exceed 40.")
        break  # break out of the while loop if length is valid
    except ValueError as e:
        print(f"Error: {e} Please retry.")

# Define character sets
all_characters = string.ascii_letters + string.digits + string.punctuation
# print(f"{all_characters}")

# Generate password at desired length with at least one of each character type for added security
while True:
    password = ''.join(random.choice(all_characters)
                       for _ in range(length))

 # Enhance password strength
 # Check if the password contains at least one lowercase, one uppercase, one digit, and one special character
 # any() is a built-in Python function that returns True if at least one element of the iterable is True, else returns False
 # The while loop will keep running (regenerating the password) until the password meets all four conditions
    if (any(c.islower() for c in password) and
        any(c.isupper() for c in password) and
        any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password)):
        break  # break out of the while loop if password meets all conditions

# Display generated password
print(f"Generated password: {password}")
