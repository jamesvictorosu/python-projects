# JVM Display Even Numbers program
# This is a simple program to display even numbers within a range + the count of even numbers
# The code shows two approaches to achieve the same results:  using a for loop and using a while loop

# Using a for loop
count = 0
for number in range(1, 11):
    if number % 2 == 0:
        count += 1
        print("The number " + str(number) + " is divisible by 2")
# formatted string
print(f"We have {count} even numbers")


# Using a while loop
count = 0
number = 1
while number <= 10:
    if number % 2 == 0:
        count += 1
        print("The number " + str(number) + " is divisible by 2")
        print(f"The number {number} is divisible by 2")
    number += 1
# formatted string
print(f"We have {count} even numbers")
