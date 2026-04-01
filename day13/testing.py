class Student:
    def __init__(self, name, usn):
        self.name = name
        self.usn = usn

    def study(self):
        print(f"{self.name} (USN: {self.usn}) is studying... 📚")

    def __str__(self):
        return f"Student(name={self.name}, usn={self.usn})"

s1 = Student("Alice", "1RV17CS001")
print(s1)