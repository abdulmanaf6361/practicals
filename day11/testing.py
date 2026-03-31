class Question:

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

    def display(self): # instance method — takes self
        print(f"  Q ({self.question_type}, {self.marks}m): {self.text}")

    @classmethod # class method — takes cls instead of self
    def create_mcq(cls, text, marks=1):
        """Shortcut to create an MCQ question."""
        return cls(text, 'mcq', marks)

    @classmethod
    def create_text(cls, text, marks=5):
        """Shortcut to create a text question."""
        return cls(text, 'text', marks)

    @staticmethod # static method — no self, no cls
    def is_valid_type(q_type):
        """Static — no self, no cls. Pure utility function."""
        return q_type in ['mcq', 'text']

    def create_obj(self, cls):
        """Instance method trying to create another object (unusual)."""

        return cls("hello","text",2)

q1 = Question("What is Python?", "mcq",  2)  # This will raise NameError
q2 = q1.create_obj(Question)
q1.display()
q2.display()