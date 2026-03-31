items = ["apple", "banana"]

def add_item(lst):
    lst.append("cherry")   # modifies the original list

add_item(items)
print(items)
