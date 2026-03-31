class Relative:
    def ask_shaadi(self):
        print("Beta, shaadi kab hai?")

class Nani(Relative):
    def ask_shaadi(self):  # Overrides parent method
        print("Meri aankhon se dekh loon tera jooda... (starts crying)")

class Chacha(Relative):
    def ask_shaadi(self):
        print("Shaadiyon mein inflation aa gayi hai. Gold le le abhi.")

class CoolCousin(Relative):
    def ask_shaadi(self):
        print("Bhai chhod shaadi. Kab job milegi? Sponsor karega?")

class LittleKid:  # Not even related class — still works!
    def ask_shaadi(self):
        print("Bhaiya, shaadi mein cake milega? Mujhe cake chahiye.")

kid = LittleKid()
kid.ask_shaadi()

cousin = CoolCousin()
cousin.ask_shaadi()