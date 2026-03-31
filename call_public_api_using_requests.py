import requests
url = "https://api.github.com/users/abdulmanaf6361"
response = requests.get(url)
# print(response.status_code, "\n")
# print(response.json(), "\n")
# print(type(response.json()), "\n")

# data = response.json()
# print("name" + ": " + data["name"])
# print("repositories" + ": " + data["public_repos"])
response_dict = response.json()
# print(response_dict)
# print(type(response_dict))
id = response_dict["id"]
print("id" + ": " + str(id))
type = response_dict["type"]
print("type" + ": " + type)
company = response_dict["company"]
print("company" + ": " + str(company))
location = response_dict["location"]
print("location" + ": " + str(location))
twitter_username = response_dict["twitter_username"]
print("twitter_username" + ": " + str(twitter_username))