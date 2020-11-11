"""
Author: Alex Alvarado
Program: SalariedEmployee.py
Date: 11-7-20
Description: Salaried Employee Class
"""
from Inheritance.Employee import Employee
from datetime import date
class SalariedEmployee(Employee):
    """Salaried Employee class"""
    def __init__(self, lname, fname, s_date, salary):
        """
        :param lname: String
        :param fname: String
        :param s_date: datetime
        :param salary: Int
        """
        super().__init__(lname, fname)
        self.start_date = s_date
        self.salary = salary

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value

    def give_raise(self, value):
        if value <= self.salary:
            raise ValueError("salary cannot be lower than current value")
        self.salary = value

    def display(self):
        return Employee.display(self) + ", " + str(self.start_date) + ", $" + str(self.salary) + "/year"


#Driver

salaried_employee = SalariedEmployee("Alex", "Alvarado", date.today(), 40000)
print(salaried_employee.display())
salaried_employee.give_raise(45000)
print(salaried_employee.display())
del salaried_employee


