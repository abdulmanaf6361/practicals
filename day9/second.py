list1 = [10, 20, 30]
list2 = list1         # BUG: this is NOT a copy!

list2 = list1.copy()
list2.append(99)

print(list1)   # Expected: [10, 20, 30]   Got: [10, 20, 30, 99]
print(list2)   # Expected: [10, 20, 30, 99]
