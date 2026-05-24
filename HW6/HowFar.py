# Name: 
# Assignment: PROG1003 - HW6 - How Far

import csv
import math


# find distance between two cities
def calc_distance(a_lat, a_lon, b_lat, b_lon):
    R = 6371.0
    a_lat = math.radians(a_lat)
    a_lon = math.radians(a_lon)
    b_lat = math.radians(b_lat)
    b_lon = math.radians(b_lon)

    dlat = b_lat - a_lat
    dlon = b_lon - a_lon
    x = math.sin(dlat / 2) ** 2 + math.cos(a_lat) * math.cos(b_lat) * math.sin(dlon / 2) ** 2
    return R * 2 * math.asin(math.sqrt(x))

# load csv file
def read_file(filename):
    cities = []
    with open(filename, newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        reader.fieldnames = [name.strip() for name in reader.fieldnames]  # fix header spacing
        for row in reader:
            cities.append([row["City"], row["Country"], float(row["Latitude"]), float(row["Longitude"])])
    return cities

# main part
def main():
    data = read_file("WorldCities.csv")

    while True:
        name = input('Enter a city, "list" to see all, or "quit" to exit: ').strip()

        if name == "":
            continue
        if name.lower() == "quit":
            break
        if name.lower() == "list":
            for c in data:
                print("  " + c[0])
            continue

        index = -1
        for i in range(len(data)):
            if data[i][0].lower() == name.lower():
                index = i
                break

        if index == -1:
            print("City not found.\n")
            continue

        print(data[index][0], "found at index", index)
        start = data[index]
        dist_list = []

        for i in range(len(data)):
            if i == index:
                continue
            end = data[i]
            d = calc_distance(start[2], start[3], end[2], end[3])
            dist_list.append([d, end[0], end[1]])

        dist_list.sort()

        for d in dist_list[:13]:
            print("  {:3.4f} km to {}, {}".format(d[0], d[1], d[2]))

if __name__ == "__main__":
    main()