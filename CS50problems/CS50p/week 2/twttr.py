def main():
    word = input("Input: ")
    print(f"Output: shorten(word)")

def shorten(word):
    vowels = "AEIOUaeiou"
    new_string = ""
    for char in word:
        if char not in vowels:
            new_string+= char
    return new_string


if __name__ == "__main__":
    main()