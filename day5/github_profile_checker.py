import requests

url = "https://api.github.com/users/YOUR_USERNAME"
data = requests.get(url).json()

name = data.get("name")
login = data.get("login")
followers = data.get("followers", 0)
repos = data.get("public_repos", 0)
location = data.get("location")

print("\n--- GitHub Profile ---")
print("Name:", name)
print("Username:", login)
print("Followers:", followers)

# Condition 1
if followers > 10:
    print("Popular user!")
else:
    print("Keep growing!")

# Condition 2
if repos > 5:
    print("Active contributor!")
else:
    print("Just getting started!")

# Condition 3
if location is not None:
    print("Location:", location)
else:
    print("Location not set")