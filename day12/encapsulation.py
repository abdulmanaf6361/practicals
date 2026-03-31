class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # __ = PRIVATE. Hands off!

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}. Nice, you're not broke!")

    def get_balance(self):
        return self.__balance  # Only I can share MY balance

acc = BankAccount("Raju", 500)
acc.deposit(200)
print(acc.get_balance())   # ✅ 700
print(acc.__balance)     # ❌ AttributeError — CAUGHT!


class Amma:
    def __init__(self):
        self.__secret_cash = 50000   # private! nobody knows
        self.__gold = "22 sovereigns"  # for "daughter's wedding only"

    def request_money(self, reason):
        if reason == "fees":
            return f"Okay, take ₹{self.__secret_cash}. Don't tell Appa."
        elif reason == "phone":
            return "Paisa tree-la grow aaguthaa?? NO."
        else:
            return "First get 90% in exam. Then we'll see."

amma = Amma()
print(amma.request_money("fees"))
print(amma.request_money("phone"))