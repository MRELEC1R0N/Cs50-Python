from seasons import check_birthday


def main():
    test_check_birthday()

def test_check_birthday():
    assert  check_birthday("2005/19/05") == None
    assert  check_birthday("may 05,19") == None
    assert  check_birthday("2005-5-19") == None
