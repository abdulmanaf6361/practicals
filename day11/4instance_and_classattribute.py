class Question:
    print("Class is loaded")
    # ── CLASS ATTRIBUTES — shared by ALL Question objects ──
    VALID_TYPES   = ['mcq', 'text']   # rule for every question
    total_created = 0                   # counter for all questions

    def __init__(self, text, question_type, marks):
        if question_type not in Question.VALID_TYPES:
            raise ValueError(f"Type must be one of {Question.VALID_TYPES}")

        # ── INSTANCE ATTRIBUTES — unique to this one object ──
        self.text          = text
        self.question_type = question_type
        self.marks         = marks

        # Update the class-level counter
        Question.total_created += 1

    def display(self):
        print(f"  Q ({self.question_type}, {self.marks}m): {self.text}")


# ── Demo ──────────────────────────────────────────────────
print("Questions created:", Question.total_created)   # 0

q1 = Question("What is Python?", "mcq",  2)
q2 = Question("Explain OOP.",     "text", 5)
q3 = Question("What is a list?",  "mcq",  1)

print("Questions created:", Question.total_created)   # 3
print("Valid types:",        Question.VALID_TYPES)     # ['mcq', 'text']

# Class attr accessible from object too, but it's shared
print(q1.total_created)   # 3 — same number
print(q2.total_created)   # 3 — same number

q4 = Question("what is ur name?", "video", 2)
# This will raise ValueError:
# q4 = Question("Bad type", "video", 2)  ← ValueError