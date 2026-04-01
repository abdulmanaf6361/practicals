from abc import ABC, abstractmethod


class Wedding(ABC):
    var = 10
    @abstractmethod
    def enjoy_food(self):
        print("Enjoying food...")  # base logic (you shouldn't care)

class Child(Wedding):
    def enjoy_food(self):
        print("Eating with fingers like a child 🍽️")

ch = Child()
ch.enjoy_food()
print(ch.var)