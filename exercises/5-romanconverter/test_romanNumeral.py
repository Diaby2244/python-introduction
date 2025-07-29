from __init__ import int_to_roman


def test_int_to_roman_5():
    # Maintenant le test est correct : 1 donne bien "I"
    assert int_to_roman(1) == "I"
    assert int_to_roman(2) == "II"
    assert int_to_roman(3) == "III"
    assert int_to_roman(4) == "IV"
    assert int_to_roman(5) == "V"


def test_int_to_roman_10():
    assert int_to_roman(6) == "VI"
    assert int_to_roman(7) == "VII"
    assert int_to_roman(8) == "VIII"
    assert int_to_roman(9) == "IX"


def test_int_to_roman_20():
    assert int_to_roman(10) == "X"
    assert int_to_roman(20) == "XX"
    assert int_to_roman(30) == "XXX"


from __init__ import roman_to_int


def test_roman_to_int_5():
    assert roman_to_int("I") == 1
    assert roman_to_int("II") == 2
    assert roman_to_int("III") == 3
    assert roman_to_int("IV") == 4
    assert roman_to_int("V") == 5


def test_roman_to_int10():
    assert roman_to_int("VI") == 6
    assert roman_to_int("VII") == 7
    assert roman_to_int("VIII") == 8
    assert roman_to_int("IX") == 9


def test_roman_to_int11():
    assert roman_to_int("X") == 10
    assert roman_to_int("L") == 50
    assert roman_to_int("C") == 100
    assert roman_to_int("D") == 500




