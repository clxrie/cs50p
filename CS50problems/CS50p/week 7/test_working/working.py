import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    parts = s.split(" to ")
    if len(parts) != 2:
        raise ValueError
    time1 = parts[0]
    time2 = parts[1]

    converted1 = convert_time(time1)
    converted2 = convert_time(time2)

    return f"{converted1} to {converted2}"


def convert_time(time_str):
    matches = re.fullmatch(r"(\d{1,2})(?::(\d{2}))?\s(AM|PM)", time_str.strip())
    if not matches:
        raise ValueError
    
    hour = int(matches.group(1))
    minutes = matches.group(2)
    period = matches.group(3)

    if hour < 1 or hour > 12:
        raise ValueError
    if minutes is None:
        minutes = 0
    else:
        if int(minutes) > 59 or int(minutes) < 0:
            raise ValueError
        
    if period == "AM":
        if hour == 12:
            hour = 0

    else:
        if hour != 12:
            hour += 12

    return f"{hour:02d}:{int(minutes):02d}"
 
if __name__ == "__main__":
    main()