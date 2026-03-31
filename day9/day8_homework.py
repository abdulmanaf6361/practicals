# Part A — Integer
a = 10
print(id(a))    # ID 1
a = a + 5
print(id(a))    # ID 2 — same or different?

# Part B — List
L = [1, 2, 3]
print(id(L))    # ID 3
L.append(4)
print(id(L))    # ID 4 — same or different?

# Part C — String
s = "hello"
print(id(s))    # ID 5
s = s + " world"
print(id(s))    # ID 6 — same or different?
