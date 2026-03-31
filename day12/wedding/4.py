from abc import ABC, abstractmethod

# Abstract class
class Wedding(ABC):

    def enjoy_food(self):
        # User only calls this
        self._prepare_food()   # hidden internal step
        self._serve_food()

    @abstractmethod
    def _prepare_food(self):
        print("Default cooking...")  # base logic (you shouldn't care)

    def _serve_food(self):
        print("Food served 🍽️ Enjoy your meal!")

class BiryaniWedding(Wedding):

    def _prepare_food(self):
        print("Cooking delicious Hyderabadi Biryani 🍗🔥")

guest = BiryaniWedding()
guest.enjoy_food()
guest._prepare_food()  # ❌ Not recommended to call internal method directly
guest._serve_food()   # ❌ Not recommended to call internal method directly