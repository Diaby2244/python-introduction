class Game:
    def __init__(self, rolls: str = ""):
        self.rolls = []
        if rolls:
            self.roll(rolls)

    def roll(self, rolls: str):
        self.rolls = [char for char in rolls.replace(" ", "")]

    def char_to_value(self, c, prev=None):
        if c == 'X':
            return 10
        elif c == '/':
            return 10 - self.char_to_value(prev or self.rolls[i - 1])
        elif c == '-':
            return 0
        else:
            return int(c)
    def score(self) -> int:
        total = 0
        i = 0

        for frame in range(10):
            if self.rolls[i] == 'X':
                total += 10 + self.char_to_value(self.rolls[i + 1]) + self.char_to_value(self.rolls[i + 2], self.rolls[i + 1])
                i += 1
            elif self.rolls[i + 1] == '/':
                total += 10 + self.char_to_value(self.rolls[i + 2])
                i += 2
            else:
                total += self.char_to_value(self.rolls[i]) + self.char_to_value(self.rolls[i + 1])
                i += 2

        return total
