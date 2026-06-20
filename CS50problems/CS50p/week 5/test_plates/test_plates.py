from plates import is_valid

def test_starts_with_two_letter():
    assert is_valid("AAA") is True
    assert is_valid("1AA") is False
    assert is_valid("11A") is False
    assert is_valid("222") is False

def test_len():
    assert is_valid("AA") is True
    assert is_valid("AAAAAA") is True
    assert is_valid("A") is False
    assert is_valid("AAAAAAA") is False

def test_no_punctuation():
    assert is_valid("AA!!") is False
    assert is_valid("AA 11") is False
    assert is_valid("AA.11") is False

def test_numbers_atend():
    assert is_valid("AAB222") is True
    assert is_valid("AABB2A") is False

def test_first_number():
    assert is_valid("AA22") is True
    assert is_valid("AA022") is False


