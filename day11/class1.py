class Question:
    def __init__(self, text, q_no, question_type, marks):
        self.text          = text
        self.q_no          = q_no
        self.question_type = question_type
        self.marks         = marks

    def print_values(self):
        print(f"Q{self.q_no}: {self.text} ({self.question_type}, {self.marks} marks)")

q1 = Question("What is Python?", 1, "mcq", 2)
q2 = Question("Explain OOP.", 2, "text", 5)

print(q1.text)          # What is Python?
print(q2.question_type)  # text

q2.marks = 4
q1.print_values()   # Q1: What is Python? (mcq, 2 marks)
q2.print_values()   # Q2: Explain OOP. (text, 4 marks)