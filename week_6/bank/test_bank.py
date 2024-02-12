from bank import value


def test_greeting_1():
    assert value("hello world") == 0
    assert value("HELLO WORLD") == 0
def test_greeting_2():
    assert value("hi world") == 20
    assert value("HI WORLD") == 20
def test_greeting_3():
    assert value("wassup world") == 100
    assert value("WASSUP WORLD") == 100
