from numb3rs import validate


def test_format():
    assert validate(r'1.2.3.4') == True
    assert validate(r'512.1.1.1') == False
    assert validate(r'1.256.1') == False
    assert validate(r'256.1') == False
    assert validate(r'256') == False

def test_range():
    assert validate(r'255.255.255.255') == True
    assert validate(r'256.1.1.1') == False
    assert validate(r'1.256.1.1') == False
    assert validate(r'1.1.256.1') == False
    assert validate(r'1.1.1.256') == False
