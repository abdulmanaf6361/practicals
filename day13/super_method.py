class Father:
    def work(self):
        print("I know farming")

class Son(Father):
    def work(self):
        super().work()  # Call the parent method
        print("I know coding too! 💻")

son = Son()
son.work() 