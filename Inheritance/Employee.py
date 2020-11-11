"""
Author: Alex Alvarado
Program: Employee.py
Date: 11-7-20
Description: Employee Class
"""

class Employee:
    """Employee Class"""

    def __init__(self, lname, fname):
        """
        :param lname: String
        :param fname: String
        """
        self._last_name = lname
        self._first_name = fname


    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    def display(self):
        return "{}, {}".format(self._last_name, self._first_name)





