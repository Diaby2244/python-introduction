from src.bowling import Game

def test_sequence():
    g = Game("13 42 -/ 26 X X 3- 6/ -8 X 43")
    assert g.score() == 104


def test_gutter_game():
    g = Game("-- -- -- -- -- -- -- -- -- -- ")
    assert g.score() == 0

def test_all_ones():
    g = Game("18 11 11 11 11 11 11 11 11 11")
    assert g.score() == 27

def test_all_spares_with_5():
    g = Game("5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/5")
    assert g.score() == 150


def test_perfect_game():
    g = Game("X X X X X X X X X X X X")
    assert g.score() == 300

def test_all_nine_and_miss():
    g = Game("9- 9- 9- 9- 9- 9- 9- 9- 9- 9-")
    assert g.score() == 90

def test_spare_in_last_frame():
    g = Game("-- -- -- -- -- -- -- -- -- 5/ 5")
    assert g.score() == 15  # 10e frame = 10 + 5

def test_strike_in_last_frame():
    g = Game("-- -- -- -- -- -- -- -- -- X53")
    assert g.score() == 18  # 10e frame = 10 + 5 + 3

def test_one_strike_in_middle():
    g = Game("-- -- X 34 -- -- -- -- -- --")
    assert g.score() == 10 + 3 + 4 + 3 + 4  # 17 (strike + bonus) + 7 (frame après)

def test_two_spares_in_a_row():
    g = Game("-- -- 5/ 4/ 3- -- -- -- -- --")
    expected_score = 14 + 13 + 3  # = 30
    assert g.score() == expected_score








