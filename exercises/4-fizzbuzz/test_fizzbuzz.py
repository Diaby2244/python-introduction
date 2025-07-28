from src import *

def test_1_should_return_1():
    assert fizzbuzz(1) == "1"

def test_2_should_return_2():
    assert fizzbuzz(2) == "2"

def test_3_should_return_3():
    assert fizzbuzz(3) == "Fizz"

def test_5_should_return_Buzz():
    assert fizzbuzz(5) == "Buzz"

def test_15_should_return_FizzBuzz():
    assert fizzbuzz(15) == "FizzBuzz"

def test_fizzbuzz_from_range():
    assert fizzbuzzfrom_range(1, 15) == "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FizzBuzz"