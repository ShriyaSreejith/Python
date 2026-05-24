# PROG 1403 – Spring 2026
# HW4 – Contact List, Version 2
# Team: Shriya Sreejith, Aditi Shashidara and Lilly Ye
# Author: Shriya Sreejith, Aditi Shashidara and Lilly Ye
from datetime import datetime

class Contact:
    def __init__(self, first, last, birthdate, phone):
        self.first = first.lower()
        self.last = last.lower()
        self.birthdate = birthdate
        self.phone = phone

    def age(self):
        today = datetime.now()
        age = today.year - self.birthdate.year
        if (today.month, today.day) < (self.birthdate.month, self.birthdate.day):
            age -= 1
        return age

    def __str__(self):
        name = f"{self.last.title()}, {self.first.title()}"
        return f"{name:<30}{str(self.birthdate.date()):<12}{self.age():<5}{self.phone.formatted():<20}"