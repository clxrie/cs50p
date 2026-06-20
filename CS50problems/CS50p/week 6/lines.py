import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

lines = 0

try:
    with open(sys.argv[1],"r") as f:
        for line in f:
            if line.strip() == "":
                continue
            if line.strip().startswith("#"):
                continue
            lines +=1

except FileNotFoundError:
    sys.exit("Not a Python file")

print(lines)
   