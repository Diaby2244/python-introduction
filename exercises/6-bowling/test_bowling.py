from src.bowling import Game

def test_gutter_game():
    g = Game("-- -- -- -- -- -- -- -- -- -- ")

    assert g.score() == 0


def test_all_ones():
    g = Game("11 11 11 11 11 11 11 11 11 11")
    assert g.score() == 20
