import csv


class Student:                                                              #student class
    def __init__(self, last_name, first_name, grade, classroom,             #class initializer
                 bus, gpa, teacher_last, teacher_first):
        self.last_name = last_name                                          #last name
        self.first_name = first_name                                        #first name
        self.grade = grade                                                  #grade level
        self.classroom = classroom                                          #classroom number
        self.bus = bus                                                      #bus route number
        self.gpa = gpa                                                      #GPA
        self.teacher_last = teacher_last                                    #teacher last name
        self.teacher_first = teacher_first                                  #teacher first name


def parse_students(filename):                                               #reads file and creates object for each student
    students = []                                                           #list of student objects

    with open(filename, "r") as file:                                       #opens and reads student file
        for line in file:                                                   #loops through each line in file
            fields = line.strip().split(",")                                #formats data for student objects

            student = Student(                                              #creates student object
                fields[0].strip(),                                          #student last name
                fields[1].strip(),                                          #student first name
                int(fields[2]),                                             #student grade as int
                int(fields[3]),                                             #classroom number as int
                int(fields[4]),                                             #bus route as int
                float(fields[5]),                                           #student GPA as float
                fields[6].strip(),                                          #teacher last name
                fields[7].strip()                                           #teachers first name
            )

            students.append(student)                                        #appends student object to student list

    return students                                                         #returns list of student objects


