from src.bowling import Game

def test_gutter_game():
    g = Game()
    for _ in range(10):
        g.roll("--")
    assert g.score() == 0

def test_all_nines_and_misses():
    g = Game()
    for _ in range(10):
        g.roll("9-")
    assert g.score() == 90

def test_all_spares():
    g = Game()
    for _ in range(10):
        g.roll("5/")
    g.roll("5")
    assert g.score() == 150

def test_all_strikes():
    g = Game()
    for _ in range(12):
        g.roll("X")
    assert g.score() == 300


