# Practice 1 : Python Dictionary Task

mydata = {
    "india": {
        "capital": "New Delhi",
        "currency": "INR",
        "states": ["GUJARAT", "MAHARASHTRA", "RAJASTHAN"]
    },
    "companies": [
        {
            "name": "Google",
            "country": "USA"
        },
        {
            "name": "Infosys",
            "country": "India"
        }
    ]
}

# Print all main keys
print(mydata.keys())

# Print total number of main keys
print(len(mydata))

# Print New Delhi
print(mydata["india"]["capital"])

# Print INR
print(mydata["india"]["currency"])

# Print RAJASTHAN
print(mydata["india"]["states"][2])

# Print Google
print(mydata["companies"][0]["name"])

# Print India
print(mydata["companies"][1]["country"])

# Print total number of states
print(len(mydata["india"]["states"]))