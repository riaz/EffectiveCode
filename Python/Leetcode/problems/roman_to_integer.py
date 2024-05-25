
def roman_to_integer(s: str) -> int:
    """
    CMXIII -> 913
    """
    mapping = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000 
    }

    value = 0
    for i,c in enumerate(s):
        if i > 0 and mapping[s[i-1]] < mapping[s[i]]:
            value -= 2*mapping[s[i-1]] 
        value += mapping[c]

    return value