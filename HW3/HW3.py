#Shriya Sreejith
# HW3 - Making Change

def making_change():
    change = input("What is the amount of change you have? (0-99 cents): ")
    nickels = 0
    dimes = 0
    quarters = 0
    pennies = 0
    change = int(change)
    if change >= 25:
        quarters = change // 25
        change = change % 25
    if change >= 10:
        dimes = change // 10
        change = change % 10
    if change >= 5:
        nickels = change // 5
        change = change % 5
    if change >= 1:
        pennies = change // 1
        change = change % 1
    print("You have", quarters, "quarters,", dimes, "dimes,", nickels, "nickels, and", pennies, "pennies.")
    keepGoing = input("Do you want to continue? (y/n): ")
    if keepGoing.lower() == 'y':
        making_change()
    else:
        print("Goodbye!")

making_change()
