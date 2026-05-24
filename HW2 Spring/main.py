# PROG – Spring 2026
# HW2 – Contact List
# Solution by Shriya Sreejith

from contact import Contact
from datetime import datetime
import csv

contacts = []


print("HW2 – Contact List")
print("Solution by Shriya Sreejith")
print()

def validate_date(d):
    try:
        datetime.strptime(d, "%Y-%m-%d")
        return True
    except:
        return False

while True:
    print("\nMenu:")
    print("1. Add Contact")
    print("2. Import Contacts")
    print("3. Display Contacts")
    print("4. Export Contacts")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter choice: ").strip()
    # Add contact
    if choice == '1':  
        first = input("First name: ").strip()
        last = input("Last name: ").strip()
        birth = input("Birthdate (yyyy-mm-dd): ").strip()
        if validate_date(birth):
            contacts.append(Contact(first, last, birth))
            contacts.sort()
            print("Contact added!")
        else:
            print("Invalid date.")
    # Import
    elif choice == '2':  
        try:
            with open("Contacts.csv") as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) == 3 and validate_date(row[2]):
                        contacts.append(Contact(row[0], row[1], row[2]))
            contacts.sort()
            print("Contacts imported!")
        except FileNotFoundError:
            print("Contacts.csv not found.")
    # Display
    elif choice == '3':  
        print(f"{'Last Name':<15} {'First Name':<15} {'Birthdate':<10} {'Age':<3}")
        print("-"*45)
        for c in contacts:
            print(c)
    # Export
    elif choice == '4':  
        with open("Contacts.csv", "w", newline="") as f:
            writer = csv.writer(f)
            for c in contacts:
                writer.writerow([c.first_name, c.last_name, c.birthdate])
        print("Contacts exported!")
    # Delete
    elif choice == '5':  
        first = input("First name to delete: ").strip().lower()
        last = input("Last name to delete: ").strip().lower()
        found = None
        for c in contacts:
            if c.first_name == first and c.last_name == last:
                found = c
                break
        if found:
            confirm = input(f"Delete {found.first_name.title()} {found.last_name.title()}? (y/n): ").lower()
            if confirm == 'y':
                contacts.remove(found)
                print("Contact deleted.")
        else:
            print("Contact not found.")
    # Exit
    elif choice == '6':  
        print("HW2 Complete")
        break

    else:
        print("Invalid choice.")