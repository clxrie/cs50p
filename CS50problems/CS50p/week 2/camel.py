name = input("camelCase: ")
result = ""

for char in name:
    if char.isupper():
        result += "_" + char.lower()
    else:
        result += char

print(f"snake_case: {result}")