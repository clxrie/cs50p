from um import count

def test_count():
    assert count("um um") == 2
    assert count("um") == 1
    assert count("um um um um") == 4
    assert count("um, thanks") == 1
    assert count("um, hello, um") == 2

def test_um_inword():
    assert count("yummy") == 0
    assert count("umbrella") == 0
    assert count("album") == 0

def test_um_capital():
    assert count("Um") == 1
    assert count("UM") == 1

