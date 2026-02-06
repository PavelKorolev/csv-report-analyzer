import csv
import sys

with open(sys.argv[1], newline='') as csvfile:
    reportreader = csv.reader(csvfile)
    next(reportreader)
    max_likes = 0
    datum = ''
    for row in reportreader:
        number = int(row[1])
        if max_likes < number:
            max_likes = number
            datum = row[0]
    print(f"Maximum of likes: {max_likes}")
    print(f"Best day: {datum}")