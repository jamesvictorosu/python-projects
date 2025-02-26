# JVM Get Even Numbers program
# This program gets even numbers within a range + displays the count of even numbers
# Below are two approaches, which achieve the same result using a for loop and using a while loop
# NOTE: Printing can use string concatenation or a formatted string, with examples of both provided

# Using a for loop
count = 0  # set base count to 0 as starting point to increment from
for number in range(1, 11):
    if number % 2 == 0:
        count += 1
        print("The number " + str(number) + " is divisible by 2")

print(f"We have {count} even numbers")


# Using a while loop
count = 0  # set base count to 0 as starting point to increment from
number = 1
while number <= 10:
    if number % 2 == 0:
        count += 1
        print("The number " + str(number) + " is divisible by 2")
    number += 1

print(f"We have {count} even numbers")
