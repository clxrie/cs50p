import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)\.(\d+)", ip)
    if matches:
        for group in matches.groups():
            if len(group) > 1 and group.startswith("0"):
                return False
            if int(group) > 255:
                return False
        return True
        
    return False


if __name__ == "__main__":
    main()