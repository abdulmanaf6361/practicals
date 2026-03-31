visitors = ["alice","bob","alice","carol","bob","dave","alice"]

# 1. Total visits
print(len(visitors))

# 2. Unique visitors
unique = set(visitors)
print(unique)

# 3. Count of unique visitors
print(len(unique))

# 4. Check "eve"
print("eve" in unique)

# 5. Check "bob"
print("bob" in unique)