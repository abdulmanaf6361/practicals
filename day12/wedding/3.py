# polymorphism
class Guest:
    def eat(self):
        print("Eating food")

class SouthIndianGuest(Guest):
    def eat(self):
        print("Eating on banana leaf 🍃")

class NorthIndianGuest(Guest):
    def eat(self):
        print("Eating butter naan like a king 👑")

south_guest = SouthIndianGuest()
north_guest = NorthIndianGuest()

south_guest.eat()
north_guest.eat()