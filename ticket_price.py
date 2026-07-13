# Task 2 : Ticket Price Calculator

# Take age and ticket price from user
age = int(input("Enter your age : "))
price = float(input("Enter ticket price : "))

# No ticket charge for age below 3 years
if age < 3:
    print("No Ticket Price")

# Apply 10% discount for age between 4 and 12 years
elif age >= 4 and age <= 12:
    discount = price * 10 / 100
    final_price = price - discount
    print("Ticket Price :", final_price)

# Apply 5% discount for age above 12 years
elif age > 12:
    discount = price * 5 / 100
    final_price = price - discount
    print("Ticket Price :", final_price)

# For age 3
else:
    print("Ticket Price :", price)