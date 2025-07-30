class Game:
    def __init__(self):
        self.rolls = []

    def roll(self, frame: str):
        for char in frame:
            if char == '-':
                self.rolls.append(0)
            else:
                raise ValueError(f"Caractère non supporté : {char}")

    def score(self):
        return sum(self.rolls)

