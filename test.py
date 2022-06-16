'''
This is a temporary testing script for the API.
Run this using normal terminal (no venv).
Install requests as user in terminal beforehand.
'''
import requests

BASE = "http://127.0.0.1:5000/"

# These must be recognized as POST, GET, DELETE, or PUT
# params are case sensitive

# Add first waifu entry
test1 = requests.post(BASE + "waifulist", {"id": 1, "name": "Makise Kurisu", "anime": "Steins;Gate", "rank": 1})
print(test1.json())

# Add new waifu as best girl
# Check if rank displacement works
test2 = requests.post(BASE + "waifulist", {"id": 2, "name": "Lynn Wiles", "anime": "Pulse", "rank": 1})
print(test2.json())

# Check if ID and name repeat checks work
test3 = requests.post(BASE + "waifulist", {"id": 2, "name": "C.C.", "anime": "Code Geass", "rank": 3}) # ID check
print(test3.json())
test4 = requests.post(BASE + "waifulist", {"id": 3, "name": "Lynn Wiles", "anime": "Pulse", "rank": 1}) # Name check
print(test4.json())

# GET method test
test5 = requests.get(BASE + "waifulist", {"name": "Lynn Wiles", "anime": "Pulse"})
print(test5.json())
test6 = requests.get(BASE + "waifulist")
print(test6.json())