# Student: Maria Navarro
# Date: 2023-11-17
# Class: Python II - HW 1

from person import Person
from section import Section


class Instructor(Person):
    """
    Represents an instructor from the Person class

    Attributes:
        name (str): name of the instructor
        u_id (int): university ID of the instructor
        schedule (list): a list for the instructor's schedule of Section

    Methods:
        __init__(name, u_id): Initializes an Instructor instance with name and u_id
        add(section): adds a section to the instructor's schedule if it's not present in schedule already
        drop(section): removes a section from the instructor's schedule if it exists
        print_schedule(): prints the sections in the instructor's schedule
    """
    def __init__(self, name, u_id):
        """
        Initializes Instructor instance

        Parameters:
            name (str): name of the instructor
            u_id (int): university ID of the instructor
        """
        super().__init__(name, u_id)
        self.schedule = []

    def add(self, section):
        """
        Adds a section to the instructor's schedule if it's not present in schedule already

        Parameters:
            section (Section): section to add to schedule
        """
        if isinstance(section, Section):
            # Maria's edits
            #if section not in self.schedule:
            #    self.schedule.append(section)

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
            # Add section to schedule
            self.schedule.append(section)
            print(f"Added section {section} for instructor {self.name}")

    def drop(self, section):
        """
        Removes section from the instructor's schedule if it exists

        Parameters:
            section (Section): the section to remove
        """
        if isinstance(section, Section):
            if section in self.schedule:
                self.schedule.remove(section)
                print(f"Dropped section {section} for instructor {self.name}")

    def print_schedule(self):
        """
        Prints the sections in instructor's schedule
        """
        print(f"This is the schedule for instructor {self.name}:")
        for section in self.schedule:
            print(section)

# TEST MARIA
#if __name__ == '__main__':
#    c1 = Instructor('Maria', 4)
#    c1.add(Section('Math 001-1', 'Math 001', 'A'))
#    c1.add(Section('Math 001-2', 'Math 002', 'A'))
#    print(c1)
#    c1.print_schedule()