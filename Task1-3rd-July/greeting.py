# Task 1 : Greeting Application Based on Current Time

# Take time and AM/PM from user
time = float(input("Enter current time : "))
period = input("Enter AM or PM : ")

# Convert PM time into 24-hour format
if period == "PM" and time < 12:
    time = time + 12

# Check morning time
if time >= 6 and time < 12:
    print("Good Morning")

# Check afternoon time
elif time >= 12 and time < 16:
    print("Good Afternoon")

# Check evening time
elif time >= 16:
    print("Good Evening")

# Invalid time
else:6
    print("Invalid Time")