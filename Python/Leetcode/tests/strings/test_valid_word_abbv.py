from problems.strings.valid_word_abbv import Solution


def test_valid_word():
    s = Solution()

    word = "internationalization"
    abbr = "i12iz4n"
    assert s.validWordAbbreviation(word, abbr) == True

    word = "internationalization"
    abbr = "i5a11o1"
    assert s.validWordAbbreviation(word, abbr) == True

    word = "apple"
    abbr = "a2e"
    assert s.validWordAbbreviation(word, abbr) == False

    word = "apple"
    abbr = "a3e"
    assert s.validWordAbbreviation(word, abbr) == True

    word = "riazmunshi"
    abbr = "r3m5"
    assert s.validWordAbbreviation(word, abbr) == True

    word = "helloworld"
    abbr = "helloworld"
    assert s.validWordAbbreviation(word, abbr) == True

    word = "a"
    abbr = "b"
    assert s.validWordAbbreviation(word, abbr) == False

    word = "a"
    abbr = "a"
    assert s.validWordAbbreviation(word, abbr) == True

    word = "aabbbccccdddddeeeeee"
    abbr = "a1b2c3d4e5"
    assert s.validWordAbbreviation(word, abbr) == True

    word = "a"
    abbr = "01"
    assert s.validWordAbbreviation(word, abbr) == False
    
    word = "bignumberhahaha"
    abbr = "999999999"
    assert s.validWordAbbreviation(word, abbr) == False

