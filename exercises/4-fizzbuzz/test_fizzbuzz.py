# test_fizzbuzz.py

from src.fizzbuzz import fizzbuzz


def test_fizzbuzz_should_return_1():
    assert fizzbuzz(1) == "1"


def test_fizzbuzz_should_return_2():
    assert fizzbuzz(2) == "2"


def test_fizzbuzz_should_return_fizz_for_3():
    assert fizzbuzz(3) == "Fizz"


def test_fizzbuzz_should_return_buzz_for_5():
    assert fizzbuzz(5) == "Buzz"


def test_fizzbuzz_should_return_fizzbuzz_for_15():
    assert fizzbuzz(15) == "FizzBuzz"


def test_fizzbuzz_should_return_fizz_for_13():  # contient un 3
    assert fizzbuzz(13) == "Fizz"


def test_fizzbuzz_should_return_buzz_for_52():  # contient un 5
    assert fizzbuzz(52) == "Buzz"


def test_fizzbuzz_should_return_fizzbuzz_for_35():  # contient 3 et 5
    assert fizzbuzz(35) == "FizzBuzz"


