from src.bowling import Game

def test_gutter_game():
    g = Game()
    for _ in range(20):
        g.roll(0)
    assert g.score() == 0
def test_all_ones():
    g = Game()
    for _ in range(20):
        g.roll(1)
    assert g.score() == 20
def test_one_spare():
    g = Game()
    g.roll(5)
    g.roll(5)  # spare
    g.roll(3)  # bonus pour le spare
    for _ in range(17):
        g.roll(0)
    assert g.score() == 13  # 10 + 3
def test_one_strike():
    g = Game()
    g.roll(10)  # strike
    g.roll(3)
    g.roll(4)
    for _ in range(16):
        g.roll(0)
    assert g.score() == 17  # 10 + 3 + 4
