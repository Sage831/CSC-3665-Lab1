import csv


class Student:
    def __init__(
        self,
        last_name,
        first_name,
        grade,
        classroom,
        bus,
        gpa,
        teacher_last,
        teacher_first
    ):
        self.last_name = last_name
        self.first_name = first_name
        self.grade = grade
        self.classroom = classroom
        self.bus = bus
        self.gpa = gpa
        self.teacher_last = teacher_last
        self.teacher_first = teacher_first


def parse_students(filename):
    students = []

    with open(filename, "r") as file:
        for line in file:
            fields = line.strip().split(",")

            student = Student(
                fields[0].strip(),
                fields[1].strip(),
                int(fields[2]),
                int(fields[3]),
                int(fields[4]),
                float(fields[5]),
                fields[6].strip(),
                fields[7].strip()
            )

            students.append(student)

    return students

