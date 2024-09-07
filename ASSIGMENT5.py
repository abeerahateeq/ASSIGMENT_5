# Check if the number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

# Check if the number is positive, negative, or zero
if num > 0:
    print(f"{num} is Positive")
elif num < 0:
    print(f"{num} is Negative")
else:
    print(f"{num} is Zero")

# Check divisibility by 2 and 3
if num % 2 == 0 and num % 3 == 0:
    print(f"{num} is divisible by both 2 and 3")
elif num % 2 == 0:
    print(f"{num} is divisible by 2 but not by 3")
elif num % 3 == 0:
    print(f"{num} is divisible by 3 but not by 2")
else:
    print(f"{num} is not divisible by either 2 or 3")

# Age check for voting eligibility
age = int(input("Enter your age: "))
if age >= 18:
    nationality = input("Are you a Pakistani citizen? (yes/no): ").lower()
    if nationality == "yes":
        print("You are eligible to vote.")
    else:
        print("Please obtain a valid ID to vote.")
else:
    print("You are not eligible to vote.")

# Determine age group
if age >= 0 and age <= 12:
    print("You are a child.")
elif age >= 13 and age <= 19:
    print("You are a teenager.")
elif age >= 20 and age <= 59:
    print("You are an adult.")
elif age >= 60:
    print("You are a senior citizen.")
else:
    print("Invalid age.")

# Number of days in a month
month = int(input("Enter the month number (1-12): "))
if month in [1, 3, 5, 7, 8, 10, 12]:
    print("This month has 31 days.")
elif month in [4, 6, 9, 11]:
    print("This month has 30 days.")
elif month == 2:
    print("This month has 28 days.")
else:
    print("Invalid month.")

# Check if a year is a leap year or not
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
