# Student: Maria Navarro
# Date: 2023-11-17
# Class: Python II - HW 1
class Section:
    """
    Represents a class section with a section ID, course ID, and time block

    Attributes:
        section_id (str): The ID for the section
        course_id (str): the ID for the course
        time_block (str): the time of the section

    Methods:
        __init__(section_id, course_id, time_block): Initializes a Section instance with section ID, course ID and timeblock
        __str__(): Returns a string representation of the section
    """

    def __init__(self, section_id, course_id, time_block):
        """
        Initializes a Section instance
        section_id (str): the section ID
        course_id (str):  the course ID
        time_block (str):  the time block of the section
        """
        self.section_id = section_id
        self.course_id = course_id
        self.time_block = time_block

    def __str__(self):
        """
        Returns a string representation of the section

        Returns:
            str: Section
        """
        return f'{self.section_id}: {self.course_id}: {self.time_block}'
