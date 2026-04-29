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

    def find_top_student(self):
        if not self.roster:
            print("No data available.")
            return
        best_student = min(self.roster, key=lambda s: s.gwa)
        print("-" * 30)
        print(f"TOP STUDENT: {best_student.name}")
        print(f"GWA:         {best_student.gwa}")
        print("-" * 30)

if __name__ == "__main__":
    app = StudentRecord("students.txt")
    app.load_records()
    app.find_top_student()