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

def test_spare_in_last_frame():
    g = Game()
    for _ in range(9):
        g.roll("9-")  # 9 + 0 = 9
    g.roll("5/")
    g.roll("5")
    assert g.score() == 9 * 9 + 10 + 5  # 90 + 15 = 105

def test_strike_in_last_frame():
    g = Game()
    for _ in range(9):
        g.roll("9-")
    g.roll("X")
    g.roll("5")
    g.roll("3")
    assert g.score() == 9 * 9 + 10 + 5 + 3  # 90 + 18 = 108

def test_perfect_game():
    g = Game()
    g.roll("XXXXXXXXXXXX")
    assert g.score() == 300

def test_all_spares_with_5_bonus():
    g = Game()
    g.roll("5/5/5/5/5/5/5/5/5/5/5")
    assert g.score() == 150

def test_mixed_game():
    g = Game()
    g.roll("X7/9-X-88/-6XXX81")
    assert g.score() == 167  #

