#Super key word

class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

    def display_info(self):
        print(f"Studet Name: {self.name}")
        print(f"Roll Number: {self.roll}")

class Exam(Student):
    def __init__(self, name, roll,subject,marks):
        super().__init__(name, roll)
        self.subject=subject
        self.marks=marks

    def display_info(self):
        super().display_info()
        print(f"Subject: {self.subject}")
        print(f"Marks: {self.marks}")

class Sports(Student):
    def __init__(self, name, roll,sport_name,position):
        super().__init__(name, roll)
        self.sport_name=sport_name
        self.position=position

    def display_info(self):
        super().display_info()
        print(f"Sport: {self.sport_name}")
        print(f"Position: {self.position}")

exam_studet=Exam("Prajval",40,"DAA",95)
sports_student=Sports("YOB",102,"Football","Runner")

exam_studet.display_info()
print("....................")
sports_student.display_info()
