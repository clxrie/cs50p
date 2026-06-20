from datetime import date
import inflect
import sys

def main():
   birth = input("Date of Birth: ")
   birthday = parse_date(birth)
   minutes = calculate_minutes(birthday)
   print(minutes_to_words(minutes))

def parse_date(date_str):
    try:
        return date.fromisoformat(date_str)
    except ValueError:
        sys.exit("Invalid date")

def calculate_minutes(birthday):
    today = date.today()
    days = (today - birthday).days
    return days * 24 * 60

def minutes_to_words(minutes):
    p = inflect.engine()
    words = p.number_to_words(minutes, andword="").capitalize()
    return f"{words} minutes"

if __name__ == "__main__":
    main()
