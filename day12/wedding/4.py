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
        # write logic here


    def _serve_food(self):
        print("Food served 🍽️ Enjoy your meal!")

class BiryaniWedding(Wedding):

    def _prepare_food(self):
        print("Cooking Biryani... 🥘")

guest = BiryaniWedding()
guest.enjoy_food()
# wedding = Wedding()