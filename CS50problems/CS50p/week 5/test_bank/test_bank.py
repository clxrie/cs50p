from bank import value
import pytest

def test_value():
    assert value("hello") == 0
    assert value("hey, world") == 20
    assert value("naman") == 100
    assert value("Hello") == 0
    
    with pytest.raises(ValueError):
        raise ValueError
