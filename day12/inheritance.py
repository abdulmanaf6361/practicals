class IndianParent:
    def __init__(self, name):
        self.name = name
        self.whatsapp_forwards = 9999

    def give_gyan(self):
        print(f"{self.name}: Hamare zamane mein internet nahi tha,")
        print("phir bhi hum first class aaye. Samjhe?")

    def compare_to_sharma_ji(self):
        print("Sharma ji ka beta IIT mein hai. Tu kya kar raha hai?")

class DesiSon(IndianParent):  # Inherits everything — no choice
    def exist(self):
        print(f"{self.name} is just trying his best, okay?")
        print(f"(forwarding {self.whatsapp_forwards} msgs inherited from dad)")

beta = DesiSon("Rahul")
beta.give_gyan()         # FREE — inherited from IndianParent!
beta.compare_to_sharma_ji()   # Also inherited. Painful, but free.
beta.exist()             # His own method — small victory