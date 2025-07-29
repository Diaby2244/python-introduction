# roman_converter.py

def int_to_roman(number: int) -> str:
    res = ""
    while number >= 10:
        res += 'X'
        number -= 10

    if number == 9:
        res += 'IX'
        number -= 9

    if number >= 4:
        if number >= 5:
            res += 'V'
            number -= 5
        else:
            res += 'IV'
            number -= 4

    while number > 0:
        res += 'I'
        number -= 1

    return res


def roman_to_int(roman: str) -> int:
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
    }

    total = 0
    prev_value = 0

    for char in reversed(roman):
        value = roman_map[char]
        if value < prev_value:
            total -= value
        else:
            total += value
            prev_value = value

    return total