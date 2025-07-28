def fizzbuzz(n):
    """
    Retourne 'Fizz', 'Buzz', 'FizzBuzz', ou le nombre sous forme de chaîne.
    """
    str_n = str(n)
    fizz = (n % 3 == 0) or ('3' in str_n)
    buzz = (n % 5 == 0) or ('5' in str_n)

    if fizz and buzz:
        return "FizzBuzz"
    elif fizz:
        return "Fizz"
    elif buzz:
        return "Buzz"
    else:
        return str(n)  # <--- important !
