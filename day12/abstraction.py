from abc import ABC, abstractmethod

class Remote(ABC):  # Abstract base class
    @abstractmethod
    def press_button(self):
        pass  # "I refuse to do the work myself."

class TVRemote(Remote):
    def press_button(self):
        print("Channel changed! Netflix it is 🎬")

class ACRemote(Remote):
    def press_button(self):
        print("Temperature set to 16°C (for the drama)")

tv = TVRemote()
ac = ACRemote()
tv.press_button()   # Channel changed!
ac.press_button()   # Temperature set!

# Remote()  ← ❌ Can't instantiate abstract class!