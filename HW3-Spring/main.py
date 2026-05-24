# PROG – Spring 2026
# HW3 – Vehicle Sales
# By Shriya Sreejith


import os
from brand import VehicleBrand

MONTHS = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

def print_intro():
    print("HW3 - Vehicle Sales")
    print("Solution by Your Full Name")
    print()

def load_vehicle_data(filename):
    if not os.path.isfile(filename):
        print("File not found.")
        return {}

    brands_dict = {}
    try:
        with open(filename, "r") as f:
            lines = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"Error reading file: {e}")
        return {}

    # Find header line
    header_idx = 0
    for i, line in enumerate(lines):
        if "Jan" in line and "Feb" in line and "Mar" in line:
            header_idx = i
            break

    for line in lines[header_idx + 1:]:
        parts = line.split("\t")
        if len(parts) < 13:
            continue

        full_name = parts[0].strip()
        tokens = full_name.split(" ", 1)
        if len(tokens) < 2:
            continue
        brand_name = tokens[0].strip()
        model_name = tokens[1].strip()

        monthly_sales = []
        for val in parts[1:13]:
            val_clean = val.replace(",", "").replace("-", "0").strip()
            try:
                monthly_sales.append(int(val_clean))
            except ValueError:
                monthly_sales.append(0)

        if brand_name not in brands_dict:
            brands_dict[brand_name] = VehicleBrand(brand_name)
        brands_dict[brand_name].add_model(model_name, monthly_sales)

    return brands_dict

def display_annual_all(brands_dict):
    print("\nAnnual Sales Data for All Brands")
    print(f"{'Brand':<20} {'Model':<25} {'Annual Sales':>12}")
    print("-" * 60)
    for brand in brands_dict.values():
        print(f"\n{brand.brand_name}")
        for model in brand.models:
            print(f"  {model.model_name:<23} {model.annual_sales():>12,}")
        print(f"  {'Total':<23} {brand.annual_total():>12,}")

def display_monthly_all(brands_dict):
    print("\nMonthly Sales Data for All Brands")
    for brand in brands_dict.values():
        print(f"\n{brand.brand_name}")
        print(f"  {'Model':<25} " + " ".join(f"{m:>7}" for m in MONTHS))
        print("  " + "-" * 110)
        for model in brand.models:
            months = " ".join(f"{v:>7,}" for v in model.monthly_sales())
            print(f"  {model.model_name:<25} {months}")
        totals = " ".join(f"{v:>7,}" for v in brand.monthly_totals())
        print(f"  {'Totals':<25} {totals}")

def choose_brand(brands_dict):
    names = list(brands_dict.keys())
    # Display in two columns
    half = (len(names) + 1) // 2
    print("\nSelect a brand from this list by name or number:")
    for i in range(half):
        left = f"{i+1} - {names[i]}"
        if i + half < len(names):
            right = f"{i+half+1} - {names[i+half]}"
        else:
            right = ""
        print(f"  {left:<30} {right}")
    
    choice = input("\nChoose a brand by entering its name or number: ").strip()
    try:
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(names):
                return brands_dict[names[idx]]
            else:
                print("Number out of range.")
                return None
        elif choice in brands_dict:
            return brands_dict[choice]
        else:
            print("Invalid selection.")
            return None
    except Exception as e:
        print(f"Error selecting brand: {e}")
        return None

def display_annual_brand(brand_obj):
    print(f"\nAnnual Sales for All Models of one Brand")
    print(f"{'Brand':<15} {'Model':<25} {'Annual Sales':>12}")
    print("-" * 55)
    print(f"{brand_obj.brand_name}")
    for model in brand_obj.models:
        print(f"  {model.model_name:<23} {model.annual_sales():>12,}")
    print(f"  {'Total':<23} {brand_obj.annual_total():>12,}")

def display_monthly_brand(brand_obj):
    print(f"\nMonthly Sales for All Models of one Brand")
    print(f"  {'Brand':<15} {'Model':<20} " + " ".join(f"{m:>7}" for m in MONTHS))
    print("  " + "-" * 110)
    print(f"  {brand_obj.brand_name}")
    for model in brand_obj.models:
        months = " ".join(f"{v:>7,}" for v in model.monthly_sales())
        print(f"  {model.model_name:<34} {months}")
    totals = " ".join(f"{v:>7,}" for v in brand_obj.monthly_totals())
    print(f"  {'Totals':<34} {totals}")

def main_menu():
    print_intro()
    brands_dict = {}
    while True:
        print("\nChoose an action from this list by its number:")
        print("1 - Import Vehicle Sales Data")
        print("2 - Display annual Sales Data for all Brands")
        print("3 - Display monthly Sales Data for all Brands")
        print("4 - Display annual Sales Data by Model for one Brand")
        print("5 - Display monthly Sales Data by Model for one Brand")
        print("0 - Exit")

        choice = input("Select an action by its number: (0-5) ").strip()

        if choice == "1":
            filename = input("Enter filename (include .txt): ").strip()
            brands_dict = load_vehicle_data(filename)
            if brands_dict:
                print("Data imported successfully.")
            else:
                print("No data loaded.")
        elif choice == "2":
            if brands_dict:
                display_annual_all(brands_dict)
            else:
                print("Please import data first.")
        elif choice == "3":
            if brands_dict:
                display_monthly_all(brands_dict)
            else:
                print("Please import data first.")
        elif choice == "4":
            if brands_dict:
                brand = choose_brand(brands_dict)
                if brand:
                    display_annual_brand(brand)
            else:
                print("Please import data first.")
        elif choice == "5":
            if brands_dict:
                brand = choose_brand(brands_dict)
                if brand:
                    display_monthly_brand(brand)
            else:
                print("Please import data first.")
        elif choice == "0":
            print("HW3 Complete")
            break
        else:
            print("Invalid choice. Please enter a number 0-5.")

if __name__ == "__main__":
    main_menu()