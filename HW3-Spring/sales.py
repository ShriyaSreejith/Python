# PROG - Spring 2026
# HW3 – Vehicle Sales
# By Shriya Sreejith

class VehicleSales:
    def __init__(self, monthly_numbers):
        if len(monthly_numbers) != 12:
            raise ValueError("Need 12 monthly values")
        self.monthly_numbers = monthly_numbers

    def total_annual(self):
        return sum(self.monthly_numbers)

    def get_months(self):
        return self.monthly_numbers