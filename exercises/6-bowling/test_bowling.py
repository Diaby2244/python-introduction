from src.bowling import Game

def test_gutter_game():
    g = Game()
    for _ in range(10):
        g.roll("--")
    assert g.score() == 0
