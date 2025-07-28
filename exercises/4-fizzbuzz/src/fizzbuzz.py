def fizzbuzz(number: int) -> str:
    """
    Retourne 'Fizz' si le nombre est multiple de 3 ou contient 3,
    'Buzz' s'il est multiple de 5 ou contient 5,
    'FizzBuzz' si les deux conditions sont vraies,
    sinon retourne le nombre sous forme de chaîne.
    """
    result = ""

    if number % 3 == 0 or '3' in str(number):
        result += "Fizz"
    if number % 5 == 0 or '5' in str(number):
        result += "Buzz"

    return result or str(number)


def compute() -> None:
    """
    Affiche la séquence FizzBuzz de 1 à 100.
    """
    for i in range(1, 101):
        print(fizzbuzz(i))
