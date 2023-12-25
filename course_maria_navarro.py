# Student: Maria Navarro
# Date: 2023-11-17
# Class: Python II - HW 1
class Course:
    """
    A class that represents a course with a unique course ID, name, and number of credits.

    Attributes:
        course_id (str): The ID for the course
        name (str): The name of the course
        number_of_credits (int): The number of credits assigned to the course

    Methods:
        __init__(course_id, name, number_of_credits):
            Initializes a new Course instance with the course information and assigns attributes to instance variables
        __str__():
            Returns a string representation of the course containing course ID, name, and credits.

    """
    def __init__(self, course_id, name, number_of_credits):
        """
        Initializes instance of the Course class

        Parameters:
        course_id (str): Course ID
        name (str): Course Name
        number_of_credits (int): Number of credits
        """
        self.course_id = course_id
        self.name = name
        self.number_of_credits = number_of_credits

    def __str__(self):
        """
        Returns a string representation of the course

        Returns:
            str: Course information
        """
        return f'{self.course_id}: {self.name}: {self.number_of_credits}'


#if __name__ == '__main__':
#    c1 = Course('DYN401', 'Digital Signal Processing (DSP)', 4)
#    c2 = Course('DYN402', 'DSP Laboratory', 2)
#    c3 = Course('DYN403', 'Sprectral Analysis', 4)
#    print(c1)
#    print(c2)
#    print(c3)
