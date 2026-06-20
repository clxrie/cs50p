from numb3rs import validate

def test_valid():
    assert validate("1.2.3.4") is True
    assert validate("0.0.0.0") is True
    assert validate("13.13.13.13") is True
    assert validate("145.232.32.42") is True
    assert validate("165.223.39.4") is True
    assert validate("230.22.38.40") is True

def test_invalid():
    assert validate("256.1.1.54") is False
    assert validate("1.256.1.54") is False
    assert validate("99.67.256.54") is False
    assert validate("78.145.13.256") is False

def test_invalidformat():
    assert validate("78.145.13") is False
    assert validate("78.145.13.43.22") is False
    assert validate("78.145.13.abc") is False
    assert validate("78.145.13.") is False
    assert validate(".145.13.43") is False
    assert validate("78..145.13") is False