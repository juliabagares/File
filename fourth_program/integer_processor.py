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