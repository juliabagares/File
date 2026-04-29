class LifeRecorder:
    def __init__(self, filename="mylife.txt"):
        self.filename = filename

    def start_session(self):
        print(f"Welcome to LifeRecorder(saving to {self.filename})")

        with open(self.filename, "a") as file:
