from src.bowling import Game

def test_gutter_game():
    g = Game("-- -- -- -- -- -- -- -- -- -- ")
    assert g.score() == 0

def test_all_ones():
    g = Game("11 11 11 11 11 11 11 11 11 11")
    assert g.score() == 20

def test_all_spares_with_5():
    g = Game("5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/5")
    assert g.score() == 150


def test_perfect_game():
    g = Game("X X X X X X X X X X X X")
    assert g.score() == 300

def test_all_nine_and_miss():
    g = Game("9- 9- 9- 9- 9- 9- 9- 9- 9- 9-")
    assert g.score() == 90
