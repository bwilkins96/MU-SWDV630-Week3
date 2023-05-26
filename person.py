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
        self._unpaid_hours = 0
        self._unpaid_overtime = 0

        super().__init__(*args, **kwargs)

    def get_pay_rate(self):
        return self._pay_rate
    
    def set_pay_rate(self, pay_rate):
        self._pay_rate = pay_rate

    def add_hours(self, hours, overtime=0):
        self._unpaid_hours += hours
        self._unpaid_overtime += overtime

    def reset_hours(self):
        self._unpaid_hours = 0
        self._unpaid_overtime = 0

    def get_total_pay(self):
        rate = self.get_pay_rate()
        total = (self._unpaid_hours * rate) + (self._unpaid_overtime * rate * 1.5)
        return total