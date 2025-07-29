# Placez ce code dans votre fichier source, par exemple __init__.py ou roman_converter.py

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


    return res # Retourne le chiffre romain construit