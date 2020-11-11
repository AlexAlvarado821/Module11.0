"""
Author: Alex Alvarado
Program: HourlyEmployee.py
Date: 11-7-20
Description: HourlyEmployee Class which inherits from Employee
"""
from Inheritance.Employee import Employee
from datetime import date

class HourlyEmployee(Employee):
    """HourlyEmployee class"""
    def __init__(self, lname, fname, start_date, hourly_pay):
        """
        :param lname: String
        :param fname: String
        :param start_date: datetime
        :param hourly_pay: float
        """
        super().__init__(lname, fname)
        self.start_date = start_date
        self.hourly_pay = hourly_pay

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value

    @property
    def hourly_pay(self):
        return self._hourly_pay

    @hourly_pay.setter
    def hourly_pay(self, value):
        if not isinstance(value, float):
            raise ValueError("the pay is not a float")
        self._hourly_pay = value

    def give_raise(self, value):
        if value <= self.hourly_pay:
            raise ValueError("pay rate needs to be greater than the current pay rate")
        self.hourly_pay = value
    def display(self):
        return Employee.display(self) + ", " + str(self.start_date) + ", $" + str(self.hourly_pay) + "/hr"



#Driver
h_employee = HourlyEmployee("Alex", "Alvarado", date.today(), 10.00)
print(h_employee.display())
h_employee.give_raise(12.00)
print(h_employee.display())
del h_employee
