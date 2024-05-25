from problems import roman_to_integer

def test_roman_to_integer():
    want = "III"
    assert roman_to_integer(want) == 3

    want = "LVIII"
    assert roman_to_integer(want) == 58

    want = "MCMXCIV"
    assert roman_to_integer(want) == 1994

    want = "MMXXIV"
    assert roman_to_integer(want) == 2024