def main():
    feeling = input("")
    print(convert(feeling))

def convert(feeling):
    feeling = feeling.replace(":)", "🙂").replace(":(", "🙁")
    return feeling

main()