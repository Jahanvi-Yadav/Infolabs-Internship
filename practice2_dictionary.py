# Practice 2 : Python Dictionary Task

mydata = {
    "school": {
        "name": "ABC School",
        "classes": [
            {
                "class": "10th",
                "students": [
                    {
                        "name": "Raj",
                        "subjects": {
                            "Maths": 85,
                            "Science": 90
                        }
                    }
                ]
            },
            {
                "class": "12th",
                "students": [
                    {
                        "name": "Neha",
                        "subjects": {
                            "Physics": 88,
                            "Chemistry": 92
                        }
                    }
                ]
            }
        ]
    }
}

# Print school name
print(mydata["school"]["name"])

# Print 10th
print(mydata["school"]["classes"][0]["class"])

# Print Raj
print(mydata["school"]["classes"][0]["students"][0]["name"])

# Print Science marks
print(mydata["school"]["classes"][0]["students"][0]["subjects"]["Science"])

# Print 12th
print(mydata["school"]["classes"][1]["class"])

# Print Neha
print(mydata["school"]["classes"][1]["students"][0]["name"])

# Print Chemistry marks
print(mydata["school"]["classes"][1]["students"][0]["subjects"]["Chemistry"])

# Print all keys inside subjects
print(mydata["school"]["classes"][0]["students"][0]["subjects"].keys())

# Print total classes
print(len(mydata["school"]["classes"]))

# Print total students
print(len(mydata["school"]["classes"][0]["students"]) +
      len(mydata["school"]["classes"][1]["students"]))