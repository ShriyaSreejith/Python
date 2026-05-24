# PROG – Spring 2026
# HW3 – Vehicle Sales
# By Shriya Sreejith

from model import VehicleModel

class VehicleBrand:
    def __init__(self, brand_name):
        self.brand_name = brand_name
        self.models = []

    def add_model(self, model_name, monthly_numbers):
        self.models.append(VehicleModel(self.brand_name, model_name, monthly_numbers))

    def annual_total(self):
        return sum(m.annual_sales() for m in self.models)

    def monthly_totals(self):
        totals = [0] * 12
        for model in self.models:
            for i, val in enumerate(model.monthly_sales()):
                totals[i] += val
        return totals