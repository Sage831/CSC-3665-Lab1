

class Student:                                                                  #student class
    def __init__(self, last_name, first_name, grade, classroom,                 #class initializer
                 bus, gpa, teacher_last, teacher_first):

        self.last_name = last_name                                              #last name
        self.first_name = first_name                                            #first name
        self.grade = grade                                                      #grade level
        self.classroom = classroom                                              #classroom number
        self.bus = bus                                                          #bus route number
        self.gpa = gpa                                                          #GPA
        self.teacher_last = teacher_last                                        #teacher last name
        self.teacher_first = teacher_first                                      #teacher first name


def parse_students(filename):                                                   #reads file and creates object for each student
    students = []                                                               #list of student objects

    try:                                                                        #attempts to open student file
        with open(filename, "r") as file:                                       #opens and reads student file
            for line in file:                                                   #loops through each line in file
                fields = line.strip().split(",")                                #formats data for student objects

                if len(fields) != 8:                                            #checks for incorrect number of fields
                    print("students.txt has incorrect format")                  #prints format error
                    return None                                                 #parser failure

                student = Student(                                              #creates student object
                    fields[0].strip(),                                          #student last name
                    fields[1].strip(),                                          #student first name
                    int(fields[2]),                                             #student grade as int
                    int(fields[3]),                                             #classroom number as int
                    int(fields[4]),                                             #bus route as int
                    float(fields[5]),                                           #student GPA as float
                    fields[6].strip(),                                          #teacher last name
                    fields[7].strip()                                           #teacher first name
                )
                students.append(student)                                        #appends student object to student list

    except FileNotFoundError:                                                   #handles missing student file
        print("students.txt not found")                                         #prints error message
        return None                                                             #parser failure

    except ValueError:                                                          #handles invalid numeric data
        print("students.txt has incorrect format")                              #prints format error
        return None                                                             #parser failure

    return students                                                             #returns list of student objects


def receive_input(students):                                                    #receives and processes user inputs
    while True:                                                                 #loops until quit input
        command = input("Input Command: ").strip()                              #receives input from user

        if command == "Q" or command == "Quit":                                 #checks for quit
            break

        elif command.startswith("S:") or command.startswith("Student:"):        #checks for student
            arguments = command.split(":", 1)[1].strip().split()                #gets arguments after command

            if len(arguments) == 0:                                             #missing student name
                continue

            last_name = arguments[0]                                                                #gets student last name

            for student in students:                                                                #searches student objects
                if student.last_name == last_name:                                                  #matching student
                    if len(arguments) > 1 and (arguments[1] == "B" or arguments[1] == "Bus"):       #bus option
                        print(f"{student.last_name},{student.first_name},{student.bus}")
                    else:                                                                           #normal student search
                        print(f"{student.last_name},{student.first_name},{student.grade},{student.classroom},{student.teacher_last},{student.teacher_first}")

        elif command.startswith("T:") or command.startswith("Teacher:"):        #checks for teacher
            arguments = command.split(":", 1)[1].strip().split()                #gets arguments after command

            if len(arguments) == 0:
                continue

            teacher_last = arguments[0]                                         #gets teacher last name

            for student in students:                                            #searches all student objects
                if student.teacher_last == teacher_last:                        #matching teacher
                    print(f"{student.last_name},{student.first_name}")

        elif command.startswith("B:") or command.startswith("Bus:"):            #checks for bus route
            arguments = command.split(":", 1)[1].strip().split()                #gets arguments after command

            if len(arguments) == 0:
                continue

            try:                                                                #attempts to convert bus route to int
                bus_route = int(arguments[0])                                   #gets bus route number
            except ValueError:                                                  #handles invalid bus route
                continue                                                        #returns to input prompt

            for student in students:                                            #searches all student objects
                if student.bus == bus_route:                                    #matching bus route
                    print(f"{student.last_name},{student.first_name},{student.grade},{student.classroom}")

        elif command.startswith("G:") or command.startswith("Grade:"):          #checks for grade
            arguments = command.split(":", 1)[1].strip().split()                #gets arguments after command

            if len(arguments) == 0:                                             #checks for missing grade
                continue

            try:                                                                            #attempts to convert grade to int
                grade = int(arguments[0])                                                   #gets grade number
            except ValueError:                                                              #handles invalid grade
                continue                                                                    #returns to input prompt

            if len(arguments) > 1 and (arguments[1] == "H" or arguments[1] == "High"):      #highest GPA option
                highest_student = None                                                      #stores student with highest GPA found

                for student in students:                                                    #searches all student objects
                    if student.grade == grade:                                              #checks for matching grade
                        if highest_student is None or student.gpa > highest_student.gpa:    #checks if student has higher GPA
                            highest_student = student                                       #updates highest GPA student

                if highest_student is not None:                                             #checks that a matching student was found
                    print(f"{highest_student.last_name},{highest_student.first_name},{highest_student.gpa},{highest_student.teacher_last},{highest_student.teacher_first},{highest_student.bus}")

            elif len(arguments) > 1 and (arguments[1] == "L" or arguments[1] == "Low"):     #lowest GPA option
                lowest_student = None                                                       #stores student with lowest GPA found

                for student in students:                                                    #searches all student objects
                    if student.grade == grade:                                              #checks for matching grade
                        if lowest_student is None or student.gpa < lowest_student.gpa:      #checks if student has lower GPA
                            lowest_student = student                                        #updates lowest GPA student

                if lowest_student is not None:                                              #checks that a matching student was found
                    print(f"{lowest_student.last_name},{lowest_student.first_name},{lowest_student.gpa},{lowest_student.teacher_last},{lowest_student.teacher_first},{lowest_student.bus}")

            else:                                                               #normal grade search
                for student in students:                                        #searches all student objects
                    if student.grade == grade:                                  #checks for matching grade
                        print(f"{student.last_name},{student.first_name}")      #prints matching student name

        elif command.startswith("A:") or command.startswith("Average:"):        #checks for average
            arguments = command.split(":", 1)[1].strip().split()                #gets arguments after command

            if len(arguments) == 0:                                             #checks for missing grade
                continue

            try:                                                                #attempts to convert grade to int
                grade = int(arguments[0])                                       #gets grade number
            except ValueError:                                                  #handles invalid grade
                continue                                                        #returns to input prompt

            total_gpa = 0                                                       #stores total GPA of matching students
            student_count = 0                                                   #stores number of matching students

            for student in students:                                            #searches all student objects
                if student.grade == grade:                                      #checks for matching grade
                    total_gpa += student.gpa                                    #adds student GPA to total GPA
                    student_count += 1                                          #increments matching student count

            if student_count > 0:                                               #checks that matching students were found
                average_gpa = total_gpa / student_count                         #calculates average GPA
                print(f"{grade},{average_gpa:.2f}")                             #prints grade and average GPA

        elif command == "I" or command == "Info":                               #checks for  info
            for grade in range(7):                                              #loops through grades 0 through 6
                student_count = 0                                               #stores number of students in current grade

                for student in students:                                        #searches all student objects
                    if student.grade == grade:                                  #checks for matching grade
                        student_count += 1                                      #increments student count
                print(f"{grade}: {student_count}")                              #prints grade and number of students

        else:                                                                   #incorrect input
            continue


def main():                                                                     #runs school search program
    students = parse_students("students.txt")                                   #parses student file

    if students is not None:                                                    #checks parsing success
        receive_input(students)                                                 #starts input loop


if __name__ == "__main__":                                                      #runs main
    main()