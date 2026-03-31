class Person:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def introduce(self):
        print(f"Hi, I am {self.name}, I am the {self.role}")


M = Person("Rahul", "Groom")
F = Person("Priya", "Bride")

M.introduce()
F.introduce()


class Marriage:
    relation = ["Parents", "Siblings", "Cousins", "Friends", "Colleagues"]
    def __init__(self, F, M, budget):
        self.F = F
        self.M = M
        self.__budget = budget   # 🔥 private variable

    def show_budget(self, relation):
        if relation in Marriage.relation:
            print(f"Budget is {self.__budget}")

        else:
            print("none of ur business, chacha!")

m = Marriage(F, M, 1000000)

# m.show_budget("chacha")        # ✅ allowed
print(m.__budget)
