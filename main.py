import csv
import sys

if len(sys.argv) < 2:
    print ("too few arguments")
    exit(1)

if not sys.argv[1].endswith(".csv"):
        print("invalid format")
        exit(1)

try:
    with open(sys.argv[1], newline='') as csvfile:
        reportreader = csv.reader(csvfile)
        next(reportreader)
        max_likes = 0
        datum = ''
        for row in reportreader:
            try:
                number = int(row[1])
                if max_likes < number:
                    max_likes = number
                    datum = row[0]
            except ValueError:
                print("Invalid data in CSV")
                exit(1)
        print(f"Maximum of likes: {max_likes}")
        print(f"Best day: {datum}")
except FileNotFoundError:
    print("Cannot open file")
    exit(1)