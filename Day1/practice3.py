#Write a Python program to check if a number is Positive, Negative or Zero.
number = int(input("Type any Natural Number : "))
if number > 0:
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is negative")
else:
    print(f"{number} is zero")
