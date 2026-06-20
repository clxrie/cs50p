from working import convert
import pytest

def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("11 AM to 11 PM") == "11:00 to 23:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_convert_minutes():
    assert convert("9:43 AM to 5:59 PM") == "09:43 to 17:59"
    assert convert("10:13 AM to 10:19 PM") == "10:13 to 22:19"
    assert convert("12:43 AM to 5:59 PM") == "00:43 to 17:59"

def test_convert_raises():
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("10:60 AM to 5 PM")
