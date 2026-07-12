#online_banking system
# Assignment 01 : Online Banking System

# Predefined data
email = "admin@gmail.com"
password = "Admin@123"
account_status = "active"
age = 21
balance = 15000
daily_limit = 10000

# Take email and password from user
useremail = input("Enter your email : ")
userpassword = input("Enter your password : ")

# Check empty fields
if useremail == "" or userpassword == "":
    if useremail == "" and userpassword == "":
        print("Both fields are required*")
    elif useremail == "":
        print("Email is required*")
    else:
        print("Password is required*")

# Check login details
elif useremail == email and userpassword == password:
    print("Login Successful")

    # Check account status
    if account_status == "active":

        # Check age verification
        if age >= 18:
            print("Banking Services Available")

            # Display banking menu
            print("1. Check Balance")
            print("2. Withdraw Money")
            print("3. Deposit Money")

            choice = int(input("Enter your choice : "))

            # Check balance
            if choice == 1:
                print("Current Balance :", balance)

            # Withdraw money
            elif choice == 2:
                amount = float(input("Enter withdrawal amount : "))

                # Validate withdrawal amount
                if amount <= 0:
                    print("Invalid Withdrawal Amount")

                # Check daily limit
                elif amount > daily_limit:
                    print("Daily Limit Exceeded")

                # Check available balance
                elif amount > balance:
                    print("Insufficient Balance")

                # Update balance
                else:
                    balance = balance - amount
                    print("Withdrawal Successful")
                    print("Current Balance :", balance)

            # Deposit money
            elif choice == 3:
                amount = float(input("Enter deposit amount : "))

                # Validate deposit amount
                if amount <= 0:
                    print("Invalid Deposit Amount")

                # Update balance
                else:
                    balance = balance + amount
                    print("Deposit Successful")
                    print("Current Balance :", balance)

            # Invalid menu choice
            else:
                print("Invalid Choice")

        # Age restriction
        else:
            print("Age Restriction: You must be 18 or above")

    # Account blocked
    else:
        print("Your Account is Blocked")

# Invalid login details
else:
    print("Invalid Credentials")