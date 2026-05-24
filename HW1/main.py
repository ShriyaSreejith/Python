# PROG – Spring 2026
#Name: Shriya Sreejith
# HW1 – Counting Weekends


from datetime import datetime, timedelta

print("\nHW1 – Counting Weekends")
print("Solution by Shriya Sreejith\n")


while True:

    # Get starting date
    while True:
        start_input = input("What is the starting date?: ")
        try:
            if "-" in start_input:
                start_date = datetime.strptime(start_input, "%Y-%m-%d")

            elif start_input.count("/") == 2:
                start_date = datetime.strptime(start_input, "%m/%d/%Y")

            elif start_input.count("/") == 1:
                start_date = datetime.strptime(start_input, "%m/%d")
                start_date = start_date.replace(year=2026)

            else:
                raise ValueError

            if start_date.year < 1800 or start_date.year > 2200:
                raise ValueError

            break
        except:
            print("Invalid date. Try again.")

    # Get ending date
    while True:
        end_input = input("What is the ending date? ")
        try:
            if "-" in end_input:
                end_date = datetime.strptime(end_input, "%Y-%m-%d")

            elif end_input.count("/") == 2:
                end_date = datetime.strptime(end_input, "%m/%d/%Y")

            elif end_input.count("/") == 1:
                end_date = datetime.strptime(end_input, "%m/%d")
                end_date = end_date.replace(year=2026)

            else:
                raise ValueError

            if end_date.year < 1800 or end_date.year > 2200:
                raise ValueError

            break
        except:
            print("Invalid date. Try again.")

    # Make sure dates are in order
    if start_date > end_date:
        temp = start_date
        start_date = end_date
        end_date = temp

    print("startDate =", start_date.date())
    print("startDate =", start_date.strftime("%A"))
    print("endDate =", end_date.date())
    print("endDate =", end_date.strftime("%A"))

    # Count weekends
    full_weekends = 0
    sat_only = 0
    sun_only = 0

    current = start_date

    while current <= end_date:

        if current.weekday() == 5:
            if current + timedelta(days=1) <= end_date and (current + timedelta(days=1)).weekday() == 6:
                full_weekends += 1
                current = current + timedelta(days=1)
            else:
                sat_only += 1

        elif current.weekday() == 6:
            sun_only += 1

        current = current + timedelta(days=1)

    total = full_weekends + sat_only + sun_only

    print("Full Weekends:", full_weekends)
    print("Saturday-only Weekends:", sat_only)
    print("Sunday-only Weekends:", sun_only)
    print("Total Weekends:", total)

    again = input("Check another date range? (Y/N) ")
    if again.lower() != "y":
        break

print("HW1 Complete")
