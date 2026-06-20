from fuel import convert, gauge
import pytest

def test_convert_normal():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/4") == 25

def test_convert_round():
    assert convert("1/3") == 33
    assert convert("2/3") == 67

def test_convert_zerodivisor():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_convert_valueerror():
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ValueError):
        convert("cat/cat")
    with pytest.raises(ValueError):
        convert("-3/4")


def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"

def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"



