class Question:

    def __init__(self, text, question_type, marks):
        # self = this specific object being created
        self.text          = text
        self.question_type = question_type   # 'mcq' or 'text'
        self.marks         = marks

    def display(self):
        print(f"  Q: {self.text}")
        print(f"     Type: {self.question_type} | Marks: {self.marks}")

class Test:

    def __init__(self, title, created_by, time_limit_mins=30):
        self.title        = title
        self.created_by   = created_by
        self.time_limit   = time_limit_mins
        self.questions    = []          # starts empty
        self.is_published = False

    def add_question(self, question):
        self.questions.append(question)
        print(f"  ✓ Added: '{question.text}'")

    def total_marks(self):
        return sum(q.marks for q in self.questions)

    def publish(self):
        if not self.questions:
            print("  ✗ Can't publish — no questions!")
            return
        self.is_published = True
        print(f"  ✓ '{self.title}' is now LIVE")

    def summary(self):
        print(f"\n{'='*40}")
        print(f"  TEST    : {self.title}")
        print(f"  TEACHER : {self.created_by}")
        print(f"  TIME    : {self.time_limit} mins")
        print(f"  Q COUNT : {len(self.questions)}")
        print(f"  TOTAL   : {self.total_marks()} marks")
        print(f"  STATUS  : {'Published' if self.is_published else 'Draft'}")
        print(f"{'='*40}\n")


# ── Demo ──────────────────────────────────────────────────
q1 = Question("Python is _____ language.", "mcq",  2)
q2 = Question("What is a class?",          "text", 5)
q3 = Question("What does len() do?",       "mcq",  2)
q1.display()
q2.display()


python_quiz = Test("Python Basics Quiz", "Ravi Sir", 30)
python_quiz.add_question(q1)
python_quiz.add_question(q2)
python_quiz.add_question(q3)
python_quiz.publish()
python_quiz.summary()