# PROG – Spring 2026
# HW3 – Vehicle Sales
# By Shriya Sreejith

from sales import VehicleSales

class VehicleModel:
    def __init__(self, brand_name, model_name, monthly_numbers):
        self.brand_name = brand_name
        self.model_name = model_name
        self.sales_data = VehicleSales(monthly_numbers)

    def annual_sales(self):
        return self.sales_data.total_annual()

    def monthly_sales(self):
        return self.sales_data.get_months()