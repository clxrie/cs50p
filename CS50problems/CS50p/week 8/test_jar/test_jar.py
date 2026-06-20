import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar2 = Jar(7)
    assert jar2.capacity == 7

def test_init_invalid():
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar("cat")   

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5

def test_deposit_invalid():
    with pytest.raises(ValueError):
        jar = Jar(5)
        jar.deposit(10)

def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(3)
    assert jar.size == 7

def test_withdraw_invalid():
    with pytest.raises(ValueError):
        jar = Jar()
        jar.deposit(5)
        jar.withdraw(10)

def test_str():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"