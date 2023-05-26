# SWDV 630 - Object-Oriented Software Architecture
# Person superclass and 3 subclasses for a hotel management system

from datetime import date

class Person:
    def __init__(self, name, start, end):
        self._name = name.title() 
        self._start = start
        self._end = end

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name.title() 
        
    def get_start(self):
        return self._start
    
    def set_start(self, start):
        self._start = start

    def get_end(self):
        return self._end
    
    def set_end(self, end): 
        self._end = end

    def __repr__(self):
        return '(Person: ' + self.get_name() + ')'

class Guest(Person):
    def __init__(self, room, *args, **kwargs):
        self._room = room
        self._checked_in = False
        super().__init__(*args, **kwargs)

    def get_room(self):
        return self._room
    
    def set_room(self, room):
        self._room = room
    
    def is_checked_in(self):
        return self._checked_in
    
    def check_in(self):
        self._checked_in = True
        self.set_start(date.today())

    def check_out(self):
        self._checked_in = False
        self.set_end(date.today())

class Employee(Person):
    def __init__(self, pay_rate,  *args, **kwargs):
        self._pay_rate = float(pay_rate)
        self._unpaid_hours = 0.0
        self._unpaid_overtime = 0.0

        super().__init__(*args, **kwargs)

    def get_pay_rate(self):
        return self._pay_rate
    
    def set_pay_rate(self, pay_rate):
        self._pay_rate = float(pay_rate)

    def add_hours(self, hours, overtime=0):
        self._unpaid_hours += hours
        self._unpaid_overtime += overtime

    def reset_hours(self):
        self._unpaid_hours = 0.0
        self._unpaid_overtime = 0.0

    def get_total_pay(self):
        rate = self.get_pay_rate()
        total = (self._unpaid_hours * rate) + (self._unpaid_overtime * rate * 1.5)
        return total
    
class Manager(Employee):
    def __init__(self, office, *args, **kwargs):
        self._office = office
        self._employees = []
        super().__init__(*args, **kwargs)

    def get_office(self):
        return self._office
    
    def set_office(self, office):
        self._office = office 

    def get_employees(self):
        return self._employees[:]
    
    def add_employees(self, *args):
        for emp in args:
            if type(emp) == Employee:
                self._employees.append(emp)

    def remove_employee(self, emp):
        emp_idx = self._employees.index(emp)
        return self._employees.pop(emp_idx)

def test_guest():
    guest = Guest(150, 'Joe', date(2023, 5, 20), date(2023, 6, 1))
    print(guest.is_checked_in(), guest.get_start())     # False, 2023-05-20

    guest.check_in()
    print(guest.is_checked_in(), guest.get_start())     # True, Today's date in yyyy-mm-dd

    guest.check_out()
    print(guest.is_checked_in(), guest.get_end())       # False, Today's date in yyyy-mm-dd

def test_employee():
    emp = Employee(20, 'Jeff', date.today(), None)
    emp.add_hours(40)
    print(emp.get_total_pay())          # 800.0

    emp.add_hours(40, 5)
    print(emp.get_total_pay())          # 1750.0

    emp.reset_hours()
    print(emp.get_total_pay())          # 0.0

def test_manager():
    man = Manager('B10', 30, 'Jenny', date.today(), None)
    print(man.get_employees())          # []

    emp_a = Employee(20, 'Julian', date.today(), None)
    emp_b = Employee(20, 'Jennifer', date.today(), None)
    man.add_employees(emp_a, emp_b)
    print(man.get_employees())          # [(Person: Julian), (Person: Jennifer)]

    man.remove_employee(emp_a)
    print(man.get_employees())          # [(Person: Jennifer)]

def test():
    test_guest()
    print()
    test_employee()
    print()
    test_manager()

if __name__ == '__main__': test()