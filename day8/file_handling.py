# with open("test.txt", "r") as f:
#     print(f.read())

# with open("test.txt", "w") as f:
#     f.write("Hello")

# with open("test.txt", "a") as f:
#     f.write("oh my kadavule")

# with open("sample1.txt", "a") as f:
#     f.write("for sample")
# with open("sample1.txt", "r") as f:
#     print(f.read(4))
#     print(f.read(4))

def add_note():
    note = input("Enter note: ")
    with open("notes.txt", "a") as f:
        f.write(note + "\n")

def view_notes():
    with open("notes.txt", "r") as f:
        print(f.read())

add_note()
view_notes()