from dataclasses import dataclass

@dataclass
class Student:
    name: str
    gwa: float

class StudentRecord:
    def __init__(self, source_file = students.txt):
        self.source = source_file
        self.roster = []
