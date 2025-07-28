from numpy import number
def fizzbuzz(number: int) -> str:
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    if number % 3 == 0 :
        return "Fizz"
    if number % 5 == 0 :
        return "Buzz"



    return str(number)

def fizzbuzzfrom_range(lower: int, upper: int) -> str:
    result = ""
    for number in range(lower, upper+1):
        result +=fizzbuzz(number)
    return result