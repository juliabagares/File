class IntegerProcessor:
    def __init__(self, source="integers.txt"):
        self.source = source
        self.evens_file = "double.txt"
        self.odds_file = "triple.txt"

    @staticmethod
    def _process_logic(value):
        if value % 2 == 0:
            return "even", value ** 2
        return "odd", value ** 3

    def run(self):
        try:
            with open (self.source, "r") as src, \
                open(self.evens_file, "w") as evens, \
                open(self.odds_file, "w") as odds:
                for line in src:
                    if not line.strip(): continue

                    value = int(line.strip())
                    category, result = self._process_logic(value)

                    if category == "even":
                        evens.write(f"{result}\n")
                    else:
                        odds.write(f"{result}\n")
        except FileNotFoundError:
            print(f"The file{self.source} doesn't exist")
