import csv
import sys

if len(sys.argv) > 3:
    sys.exit("Too many arguments")
if len(sys.argv) < 3:
    sys.exit("Too few arguments")
try:
    with open(sys.argv[1]) as before:
        reader = csv.DictReader(before)
        with open(sys.argv[2], "w") as after:
            writer = csv.DictWriter(after,fieldnames=["first","last","house"])
            writer.writeheader()
            for row in reader:
                last,first = row["name"].split(", ")
                house = row["house"]
                writer.writerow({"first": first, "last": last, "house": house})

except FileNotFoundError:
    sys.exit("File not found")