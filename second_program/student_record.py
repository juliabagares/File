from dataclasses import dataclass

@dataclass
class Student:
    name: str
    gwa: float

class StudentRecord:
    def __init__(self, source_file = "students.txt"):
        self.source = source_file
        self.roster = []

    def load_records(self):
        try:
            with open(self.source, 'r') as file:
                for line in file:
                    if ',' in line:
                        name_part, gwa_part = line.rsplit(',', 1)
                        student_obj = Student(name_part.strip(), float(gwa_part.strip()))
                        self.roster.append(student_obj)
        except FileNotFoundError:
            print(f"Error: {self.source} not found.")
        except ValueError:
            print("Error: Could not process GWA numbers.")

