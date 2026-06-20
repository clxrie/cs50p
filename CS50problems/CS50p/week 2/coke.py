amount = 0
while amount < 50:
    print(f"Amount Due: {50 - amount}")
    coins = int(input("Insert Coin: "))
    if coins in [5, 10, 25]:
        amount += coins
        
print(f"Change Owed: {amount - 50}")