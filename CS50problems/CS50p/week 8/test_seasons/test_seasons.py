from seasons import parse_date, calculate_minutes, minutes_to_words
from datetime import date
import pytest

def test_parse_date():
    assert parse_date("1999-12-14") == date(1999, 12, 14)
    assert parse_date("2026-01-01") == date(2026, 1, 1)
    
def test_parse_date_invalid():
    with pytest.raises(SystemExit):
        parse_date("cat")
    with pytest.raises(SystemExit):
        parse_date("January 1, 2026")
    with pytest.raises(SystemExit):
        parse_date("01/01/2026")

def test_calculate_minutes():
    today = date.today()
    assert calculate_minutes(today) == 0

    from datetime import timedelta
    yesterday = today - timedelta(days = 1)
    assert calculate_minutes(yesterday) == 1440

def test_minutes_to_words():
    assert minutes_to_words(625720) == "Six hundred twenty-five thousand, seven hundred twenty minutes"
    assert minutes_to_words(425680) == "Four hundred twenty-five thousand, six hundred eighty minutes"