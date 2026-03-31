# ── STEP 1: Define the class (blueprint) ──────────────────

class Question:
    pass          # empty for now — valid Python


# ── STEP 2: Create objects from it ────────────────────────

q1 = Question()   # q1 is an object of type Question
q2 = Question()   # q2 is a completely separate object

print(type(q1))    # <class '__main__.Question'>
print(q1)          # <__main__.Question object at 0x...>


# ── STEP 3: Add data directly to an object ────────────────

q1.text  = "What is Python?"
q1.marks = 2

q2.text  = "Explain OOP."
q2.marks = 5

print(q1.text, q1.marks)   # What is Python? 2
print(q2.text, q2.marks)   # Explain OOP. 5

# ── Ask students: are q1 and q2 the same object? ──────────
print(q1 is q2)   # False — separate objects in memory


print(id(Question))   # 48 bytes (may vary by implementation)
print(id(Question))   # 48 bytes (may vary by implementation)

