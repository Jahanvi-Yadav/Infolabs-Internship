# Practice 4 : Python Dictionary Task

mydata = {
    "cricket": {
        "teams": [
            {
                "team": "India",
                "players": [
                    {
                        "name": "Virat",
                        "records": {
                            "runs": 13000,
                            "centuries": 50
                        }
                    }
                ]
            },
            {
                "team": "Australia",
                "players": [
                    {
                        "name": "Smith",
                        "records": {
                            "runs": 9500,
                            "centuries": 32
                        }
                    }
                ]
            }
        ]
    }
}

# Print India
print(mydata["cricket"]["teams"][0]["team"])

# Print Virat
print(mydata["cricket"]["teams"][0]["players"][0]["name"])

# Print Virat runs
print(mydata["cricket"]["teams"][0]["players"][0]["records"]["runs"])

# Print Virat centuries
print(mydata["cricket"]["teams"][0]["players"][0]["records"]["centuries"])

# Print Australia
print(mydata["cricket"]["teams"][1]["team"])

# Print Smith
print(mydata["cricket"]["teams"][1]["players"][0]["name"])

# Print Smith runs
print(mydata["cricket"]["teams"][1]["players"][0]["records"]["runs"])

# Print Smith centuries
print(mydata["cricket"]["teams"][1]["players"][0]["records"]["centuries"])

# Print total teams
print(len(mydata["cricket"]["teams"]))

# Print all keys inside records
print(mydata["cricket"]["teams"][0]["players"][0]["records"].keys())