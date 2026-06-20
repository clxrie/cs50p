from twttr import shorten

def test_shorten():
    assert shorten("misbah") == "msbh"
    assert shorten("Komal") == "Kml"
    assert shorten("HELLO") == "HLL"
    assert shorten("komal123") == "kml123"
    assert shorten("Komal!!!") == "Kml!!!"