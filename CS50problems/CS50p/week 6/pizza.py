import sys
from tabulate import tabulate
import csv


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if not (sys.argv[1]).endswith(".csv"):
    sys.exit("Not a CSV file")

rows = []

try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames
        for row in reader:
            rows.append(list(row.values()))
except FileNotFoundError:
    sys.exit("File does not exist")


print(tabulate(rows, headers=headers, tablefmt="grid" ))

