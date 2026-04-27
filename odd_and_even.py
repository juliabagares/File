class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    RESET = '\033[0m'

class NumberProcessor:
    def __init__(self, source_file="numbers.txt"):
        self.source = source_file
        self.even_numbers = []
        self.odd_numbers = []
        

