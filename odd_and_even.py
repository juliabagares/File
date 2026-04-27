class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'

class NumberProcessor:
    def __init__(self, source_file="numbers.txt"):
        self.source = source_file
        self.even_numbers = []
        self.odd_numbers = []

    def _extract_numbers(self):
        try:
            with open(self.source, "r") as file:
                return [int(line.strip()) for line in file if line.strip()]
        except FileNotFoundError:
            print (f"Error: {self.source} not found.")
            return []

    def sort_logic(self):
        raw_numbers = self._extract_numbers()
        for number in raw_numbers:
            if number % 2 == 0:
                self.even_numbers.append(str(number))
            else:
                self.odd_numbers.append(str(number))

    def export_numbers(self, even_path="even.txt", odd_path="odd.txt"):
        with open(even_path, 'w') as e_file:
            e_file.write("\n".join(self.even_storage))




