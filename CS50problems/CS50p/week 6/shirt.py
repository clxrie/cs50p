import sys
from PIL import Image, ImageOps
import os

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

_, ext1 = os.path.splitext(sys.argv[1])
_, ext2 = os.path.splitext(sys.argv[2])

if ext1.lower() not in [".jpg",".png",".jpeg"]:
    sys.exit("Invalid input")
if ext2.lower() not in [".jpg",".png",".jpeg"]:
    sys.exit("Invalid input")
if ext1.lower() != ext2.lower():
    sys.exit("Input and output have different extensions")


shirt = Image.open("shirt.png")
size = shirt.size
try:
    photo = Image.open(sys.argv[1])
    photo = ImageOps.fit(photo, size)
    photo.paste(shirt, shirt)
    photo.save(sys.argv[2])

except FileNotFoundError:
    sys.exit("File not Found")
