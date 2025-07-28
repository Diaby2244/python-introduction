def int_to_roman(num):
    valeurs = [1000, 900, 500, 400,
               100, 90, 50, 40,
               10, 9, 5, 4,
               1]
    symboles = ["M", "CM", "D", "CD",
                "C", "XC", "L", "XL",
                "X", "IX", "V", "IV",
                "I"]
    resultat = ""
    i = 0
    while num > 0:
        for _ in range(num // valeurs[i]):
            resultat += symboles[i]
            num -= valeurs[i]
        i += 1
    return resultat
