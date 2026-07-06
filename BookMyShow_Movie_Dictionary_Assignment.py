# BookMyShow Movie Dictionary Assignment

# Create movie dictionary
movie = {
    "id": 1,
    "name": "Dhurandhar The Revenge",
    "ratings": 8.0,
    "runtime": "3h 49m",
    "votes": "2.4K",
    "movietype": ["Action", "Thriller"],
    "certificate": "A",
    "release_date": "19 Mar, 2026",
    "movieAvailableIn": ["2D"],
    "languages": ["Hindi", "Telugu", "Tamil", "Kannada", "Malayalam"],
    "details": "An action thriller movie based on revenge and intense conflicts.",
    "cast": ["Ranveer Singh", "Sanjay Dutt", "R. Madhavan", "Arjun Rampal"],
    "crew": ["Aditya Dhar", "Jyoti Deshpande", "Lokesh Dhar"]
}

# Task 2 : Access Dictionary Values
print("Movie Name :", movie["name"])
print("Ratings :", movie["ratings"])
print("Runtime :", movie["runtime"])
print("Certificate :", movie["certificate"])
print("Release Date :", movie["release_date"])
print("Movie Details :", movie["details"])

# Task 3 : Access List Data Inside Dictionary
print("First Genre :", movie["movietype"][0])
print("First Language :", movie["languages"][0])
print("First Actor :", movie["cast"][0])
print("First Crew Member :", movie["crew"][0])

# Task 4 : Count Data
print("Total Cast Members :", len(movie["cast"]))
print("Total Crew Members :", len(movie["crew"]))
print("Total Languages :", len(movie["languages"]))
print("Total Movie Types :", len(movie["movietype"]))

# Task 5 : Dictionary Methods Practice
print("Movie Keys :", movie.keys())
print("Movie Values :", movie.values())
print("Movie Items :", movie.items())