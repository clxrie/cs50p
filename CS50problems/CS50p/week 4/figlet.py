import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    font = random.choice(fonts)

elif len(sys.argv) == 3:
    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid!")
    if sys.argv[2] not in fonts:
        sys.exit("Invalid!")
    font = sys.argv[2]

else:
    sys.exit("Invalid!")

figlet.setFont(font = font)
letter = input("Input: ")
print(figlet.renderText(letter))

