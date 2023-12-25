# Student: Maria Navarro
# Date: 2023-11-17
# Class: Python II - HW 1

from person import Person
from section import Section


class Student(Person):
    """
    A class that represents a student, inheriting from the Person class

    Attributes:
        name (str): The name of the student
        u_id (int): The ID of the student
        schedule (list): A list to store the schedule of Section objects

    Methods:
        __init__(name, u_id): Initializes a Student instance with name and u_id
        add(section): Adds a Section to the student's schedule if it is not already present in schedule
        drop(section): Removes a Section from the student's schedule if it exists in the schedule
        print_schedule(): Prints the sections in the student's schedule
    """
    def __init__(self, name, u_id):
        """
        Initializes instance of Student class
        Parameters:
            name (str): name of the student
            u_id (int): ID of the student
        """
        super().__init__(name, u_id)
        self.schedule = []

    def add(self, section):
        """
        Adds a Section to the student's schedule if it is not already present in the schedule

        Parameters:
            section (Section): the section to add
        """
        if isinstance(section, Section):
            # Maria's edits: detect double-booking of same course
            for current_section in self.schedule:
                if current_section.course_id == section.course_id:
                    print(
                        f"Error. {self.name} has already been registered in another section of {section.course_id}")
                    return

            # Maria's edits: detect time conflicts
            for current_section in self.schedule:
                if current_section.time_block == section.time_block:
                    print(f"Error. {self.name} has already been registered for a class with the same time block as {section.section_id}")
                    return

            # Maria's edits
            #if section not in self.schedule:
            #    self.schedule.append(section)

            # Maria's edits
            #Add section to schedule
            self.schedule.append(section)
            print(f"Added section {section} for student {self.name}")

    def drop(self, section):
        """
        Removes a section from the student's schedule if it exists in schedule

        Parameters:
            section (Section): the section to remove
        """
        if isinstance(section, Section):
            if section in self.schedule:
                self.schedule.remove(section)
                print(f"Dropped section {section} for student {self.name}")

    def print_schedule(self):
        """ Prints the sections in the student's schedule"""
        print(f"This is the schedule for student {self.name}:")
        for section in self.schedule:
            print(section)

# TEST MARIA
#if __name__ == '__main__':
#    c1 = Student('Maria', 4)
#    c1.add(Section('Math 001-1', 'Math 001', 'A'))
#    c1.add(Section('Math 001-2', 'Math 001', 'B'))
#    print(c1)
#    c1.print_schedule()