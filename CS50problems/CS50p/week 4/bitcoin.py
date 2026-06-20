import sys
import requests

if len(sys.argv) != 2:
    sys.exit("missing command-line argument")


try:
    n= float(sys.argv[1])
except ValueError:
    sys.exit("command-line argument is not a number")

response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=cd31607f7f89c19290dee3ed438c4f5ae1c6e83e2438b1dffa2b798e634c8b00")
o = response.json()

price = float(o["data"]["priceUsd"])
cost = price * n
print(f"${cost:,.4f}")