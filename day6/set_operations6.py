alice_friends = {"bob","carol","dave","eve"}
bob_friends = {"carol","frank","eve","grace"}

# 1. Mutual friends
print(alice_friends & bob_friends)
print(alice_friends.intersection(bob_friends))
# 2. All unique people
print(alice_friends | bob_friends)
print(alice_friends.union(bob_friends))

# 3. Alice only
print(alice_friends - bob_friends)
print(alice_friends.difference(bob_friends))

# 4. Check "dave" in Bob list
print("dave" in bob_friends)