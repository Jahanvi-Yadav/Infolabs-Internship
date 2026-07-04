# Task 3 : Age Classifier

# Take age from user
age = int(input("Enter your age : "))

# Check if age is between 0 and 1 years
if age >= 0 and age <= 1:
    print("Infant")

# Check if age is between 2 and 4 years
elif age >= 2 and age <= 4:
    print("Toddler")

# Check if age is between 5 and 12 years
elif age >= 5 and age <= 12:
    print("Child")

# Check if age is between 13 and 19 years
elif age >= 13 and age <= 19:
    print("Teen")

# Check if age is between 20 and 39 years
elif age >= 20 and age <= 39:
    print("Adult")

# Check if age is between 40 and 59 years
elif age >= 40 and age <= 59:
    print("Middle Age Adult")

# Check if age is 60 years or above
elif age >= 60:
    print("Senior Adult")

# Check invalid age
else:
    print("Invalid Age")