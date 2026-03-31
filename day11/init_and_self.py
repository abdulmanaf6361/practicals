class Question:

    def __init__(self, text, question_type, marks):
        # self = this specific object being created
        self.text          = text
        self.question_type = question_type   # 'mcq' or 'text'
        self.marks         = marks

    def display(self):
        print(f"  Q: {self.text}")
        print(f"     Type: {self.question_type} | Marks: {self.marks}")


# Creating objects — __init__ runs immediately
q1 = Question("What is Python?",  "mcq",  2)
q2 = Question("Explain OOP.",      "text", 5)
q3 = Question("What is a list?",   "mcq",  1)

q1.display()
q2.display()

# Access individual attributes
print(q1.marks)          # 2
print(q2.question_type)  # text

# Modify after creation
q1.marks = 3
print(q1.marks)          # 3  (q2.marks is still 5)