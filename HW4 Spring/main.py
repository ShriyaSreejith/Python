# PROG 1403 – Spring 2026
# HW4 – Contact List, Version 2
# Team: Shriya Sreejith, Aditi Shashidara and Lilly Ye
# Author: Shriya Sreejith, Aditi Shashidara and Lilly Ye

from phonenumber import PhoneNumber
from contact import Contact
from bst import BST
from datetime import datetime
import csv


def valid_date(date_str):
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        if 1800 <= date.year <= 2200:
            return date
    except:
        pass
    return None


def create_contact():
    try:
        first = input("First: ").strip()
        last = input("Last: ").strip()

        while True:
            b = input("Birthdate (YYYY-MM-DD): ").strip()
            date = valid_date(b)
            if date:
                break
            print("Invalid date. Please use YYYY-MM-DD format between 1800 and 2200.")

        while True:
            p = input("Phone: ").strip()
            try:
                phone = PhoneNumber(p)
                break
            except ValueError as e:
                print(f"Invalid phone number: {e}. Please enter 10-15 digits.")

        return Contact(first, last, date, phone)
    except Exception as e:
        print("Error creating contact:", e)
        return None


def import_contacts(tree):
    try:
        with open("Contacts.csv", newline='') as f:
            reader = csv.reader(f)
            count = 0
            for row in reader:
                if len(row) < 4:
                    continue
                first, last, date, phone = row[0], row[1], row[2], row[3]
                # Skip header row if present
                if first.lower() == "first":
                    continue
                d = valid_date(date)
                if not d:
                    continue
                try:
                    p = PhoneNumber(phone)
                    tree.insert(Contact(first, last, d, p))
                    count += 1
                except ValueError:
                    continue
        print(f"Imported {count} contact(s).")
    except FileNotFoundError:
        print("Contacts.csv not found.")
    except Exception as e:
        print("Import failed:", e)


def export_contacts(contacts):
    try:
        with open("Contacts.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            for c in contacts:
                writer.writerow([c.first, c.last, c.birthdate.date(), c.phone.digits])
        print(f"Exported {len(contacts)} contact(s).")
    except Exception as e:
        print("Export failed:", e)


def display(contacts):
    if not contacts:
        print("No contacts to display.")
        return
    print(f"\n{'Last, First':<30}{'Birthdate':<12}{'Age':<5}{'Phone'}")
    print("-" * 65)
    for c in contacts:
        print(c)
    print()


def filter_contacts(tree):
    print("Filter by: first, last, birthdate")
    field = input("Field: ").strip().lower()
    if field not in ("first", "last", "birthdate"):
        print("Invalid field.")
        return []

    value = input("Value: ").strip().lower()
    results = []
    for c in tree.inorder():
        if field == "first" and c.first == value:
            results.append(c)
        elif field == "last" and c.last == value:
            results.append(c)
        elif field == "birthdate" and str(c.birthdate.date()) == value:
            results.append(c)

    if not results:
        print("No matching contacts found.")
    return results


def delete_contact(tree):
    try:
        first = input("First: ").strip()
        last = input("Last: ").strip()

        node = tree.find(first, last)
        if node:
            confirm = input(f"Delete {first.title()} {last.title()}? (y/n): ").strip().lower()
            if confirm == 'y':
                tree.delete(first, last)
                print("Contact deleted.")
            else:
                print("Deletion cancelled.")
        else:
            print("Contact not found.")
    except Exception as e:
        print("Error:", e)


def edit_contact(tree):
    try:
        first = input("First: ").strip()
        last = input("Last: ").strip()

        node = tree.find(first, last)
        if node:
            print("Contact found. Enter new values:")
            tree.delete(first, last)
            new = create_contact()
            if new:
                tree.insert(new)
                print("Contact updated.")
            else:
                print("Update failed. Original contact removed — please re-add manually.")
        else:
            print("Contact not found.")
    except Exception as e:
        print("Error:", e)


def menu():
    print("""
1. Enter new Contact
2. Import Contacts
3. Display all Contacts
4. Export all Contacts
5. Delete Contact
6. Edit Contact
7. Display subset
8. Export subset
9. Exit""")


def main():
    print("HW4 – Contact List, Version 2")
    print("Solution by Aditi, Shriya, Lilly\n")

    tree = BST()

    while True:
        menu()
        choice = input("\nChoice: ").strip()

        if choice == '1':
            c = create_contact()
            if c:
                tree.insert(c)
                print("Contact added.")
        elif choice == '2':
            import_contacts(tree)
        elif choice == '3':
            display(tree.inorder())
        elif choice == '4':
            export_contacts(tree.inorder())
        elif choice == '5':
            delete_contact(tree)
        elif choice == '6':
            edit_contact(tree)
        elif choice == '7':
            results = filter_contacts(tree)
            if results:
                display(results)
        elif choice == '8':
            results = filter_contacts(tree)
            if results:
                export_contacts(results)
        elif choice == '9':
            break
        else:
            print("Invalid choice. Please enter a number 1-9.")

    print("HW4 Complete")


if __name__ == "__main__":
    main()