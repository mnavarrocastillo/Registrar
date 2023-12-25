# Student: Maria Navarro
# Date: 2023-11-17
# Class: Python II - HW 1

import csv

from student import Student
from instructor import Instructor
from course import Course
from section import Section


class Registrar:
    """
    Class that orchestrates student, instructor, course and section
    """

    def __init__(self):
        """
        Initializes a Registrar instance with empty dictionaries
        """
        self.students = {}
        self.instructors = {}
        self.courses = {}
        self.sections = {}

    def read_students(self, file):
        """
        Reads student data from csv file and populates the students dictionary

        Parameters:
            file (str): csv file path
        """
        with open(file, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                name = row[0]
                u_id = row[1]
                student = Student(name, u_id)
                self.students[u_id] = student
            print(f'Number of students: {len(self.students)}')

    def read_instructors(self, file):
        """
        Reads instructors data from csv file and populates the instructors dictionary

        Parameters:
            file (str): csv file path
        """
        with open(file, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                name = row[0]
                u_id = row[1]
                instructor = Instructor(name, u_id)
                self.instructors[u_id] = instructor
            print(f'Number of intructors: {len(self.instructors)}')

    def read_courses(self, file):
        """
        Reads course data from csv file and populates the courses dictionary

        Parameters:
            file (str): csv file path
        """
        with open(file, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                c_id = row[0]
                name = row[1]
                number_of_credits = int(row[2])
                course = Course(c_id, name, number_of_credits)
                self.courses[c_id] = course
            print(f'Number of Courses: {len(self.courses)}')

    def read_sections(self, file):
        """
        Reads section data from csv file and populates the sections dictionary

        Parameters:
            file (str): the csv file path
        """
        with open(file, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                s_id = row[0]
                c_id = row[1]
                time_block = row[2]
                section = Section(s_id, c_id, time_block)
                self.sections[s_id] = section
            print(f'Number of Sections: {len(self.sections)}')

def main():
    registrar = Registrar()
    registrar.read_students('data/students.csv')
    registrar.read_instructors('data/instructors.csv')
    registrar.read_courses('data/courses.csv')
    registrar.read_sections('data/sections.csv')

    while True:
        # This provides the user options to pick from
        print("\n1. Add section to student's schedule")
        print("2. Add section to instructor's schedule")
        print("3. Drop section from student's schedule")
        print("4. Drop section from instructor's schedule")
        print("5. Print student schedule")
        print("6. Print instructor schedule")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            student_id = input("Enter student's u_id: ")
            # checks if student id is valid
            if student_id in registrar.students:
                section_id = input("Enter section ID to add: ")
                # checks if section id is valid
                if section_id in registrar.sections:
                    student = registrar.students[student_id]
                    section = registrar.sections[section_id]
                    # adds section to student schedule
                    student.add(section)
                else:
                    print("Invalid section ID.")
            else:
                print("Invalid student ID.")
        elif choice == '2':
            instructor_id = input("Enter instructor's u_id: ")
            # checks if instructor id is valid
            if instructor_id in registrar.instructors:
                section_id = input("Enter section ID to add: ")
                # checks if instructor id is valid
                if section_id in registrar.sections:
                    instructor = registrar.instructors[instructor_id]
                    section = registrar.sections[section_id]
                    # adds section to instructor schedule
                    instructor.add(section)
                else:
                    print("Invalid section ID.")
            else:
                print("Invalid instructor ID.")

        elif choice == '3':
            student_id = input("Enter student's u_id: ")
            # checks if student id is valid
            if student_id in registrar.students:
                section_id = input("Enter section ID to drop: ")
                # checks if section id is valid
                if section_id in registrar.sections:
                    student = registrar.students[student_id]
                    section = registrar.sections[section_id]
                    # drops the class from student schedule
                    student.drop(section)
                else:
                    print("Invalid section ID.")
            else:
                print("Invalid student ID.")

        elif choice == '4':
            instructor_id = input("Enter instructor's u_id: ")
            # checks is instructor id is valid
            if instructor_id in registrar.instructors:
                section_id = input("Enter section ID to drop: ")
                # checks if section id is valid
                if section_id in registrar.sections:
                    instructor = registrar.instructors[instructor_id]
                    section = registrar.sections[section_id]
                    # drops section from instructor schedule
                    instructor.drop(section)
                else:
                    print("Invalid section ID.")
            else:
                print("Invalid instructor ID.")

        elif choice == '5':
            student_id = input("Enter student's u_id: ")
            # checks if student id is valid
            if student_id in registrar.students:
                student = registrar.students[student_id]
                # prints the schedule
                student.print_schedule()
            else:
                print("Invalid student ID.")

        elif choice == '6':
            instructor_id = input("Enter instructor's u_id: ")
            # checks if instructor id is valid
            if instructor_id in registrar.instructors:
                instructor = registrar.instructors[instructor_id]
                # prints the schedule
                instructor.print_schedule()
            else:
                print("Invalid instructor ID.")

        elif choice == '7':
            # gives user option to exit program
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == '__main__':
    main()
