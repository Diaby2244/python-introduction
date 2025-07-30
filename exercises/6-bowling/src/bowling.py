class Game:
    def __init__(self, rolls: str = ""):
        self.rolls = []
        if rolls:
            self.roll(rolls)

    def roll(self, rolls: str):
        # Supprimer les espaces et stocker chaque caractère
        self.rolls = [char for char in rolls.replace(" ", "")]

    def score(self) -> int:
        total = 0
        i = 0

        def char_to_value(c, prev=None):
            if c == 'X':
                return 10
            elif c == '/':
                return 10 - char_to_value(prev or self.rolls[i - 1])
            elif c == '-':
                return 0
            else:
                return int(c)

        for frame in range(10):
            if self.rolls[i] == 'X':
                total += 10 + char_to_value(self.rolls[i + 1]) + char_to_value(self.rolls[i + 2], self.rolls[i + 1])
                i += 1
            elif self.rolls[i + 1] == '/':
                total += 10 + char_to_value(self.rolls[i + 2])
                i += 2
            else:
                total += char_to_value(self.rolls[i]) + char_to_value(self.rolls[i + 1])
                i += 2

        return total
