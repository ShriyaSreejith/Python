
# PROG 1403 – Spring 2026
# HW2 – Contact List
# Solution by Shriya Sreejith

from datetime import datetime

class Contact:
    def __init__(self, first_name, last_name, birthdate):
        self.first_name = first_name.lower()
        self.last_name = last_name.lower()
        self.birthdate = birthdate  # string format "yyyy-mm-dd"

    def age(self):
        birth_year = int(self.birthdate[:4])
        current_year = datetime.now().year
        return current_year - birth_year

    def __str__(self):
        return f"{self.last_name.title():<15} {self.first_name.title():<15} {self.birthdate} {self.age():<3}"

    # Optional: for sorting
    def __lt__(self, other):
        return (self.last_name, self.first_name) < (other.last_name, other.first_name)