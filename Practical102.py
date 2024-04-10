class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

class TopFiveStudents(Student):
    def __init__(self, *args):
        super().__init__(*args)

    def display_top_five(self):
        top_five = sorted(self.marks.items(), key=lambda x: x[1], reverse=True)[:5]
        print("Top Five Students:")
        for name, marks in top_five:
            print("Name:", name, "| Marks:", marks)

# Example usage:
student1 = TopFiveStudents("Alice", {"Math": 90, "Science": 95, "English": 85})
student2 = TopFiveStudents("Bob", {"Math": 85, "Science": 80, "English": 90})
student3 = TopFiveStudents("Charlie", {"Math": 80, "Science": 85, "English": 88})
student4 = TopFiveStudents("David", {"Math": 92, "Science": 88, "English": 91})
student5 = TopFiveStudents("Eve", {"Math": 88, "Science": 90, "English": 87})

student1.display_top_five()
