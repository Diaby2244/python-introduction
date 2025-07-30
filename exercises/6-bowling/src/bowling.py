class Game:
    def __init__(self):
        self.rolls = []

    def roll(self, frame_result: str):
        for i, char in enumerate(frame_result):
            if char == 'X':
                self.rolls.append(10)
            elif char == '-':
                self.rolls.append(0)
            elif char.isdigit():
                self.rolls.append(int(char))
            elif char == '/':
                prev = self.rolls[-1]
                self.rolls.append(10 - prev)

    def score(self):
        score = 0
        i = 0
        for frame in range(10):
            if self.rolls[i] == 10:  # strike
                score += 10 + self.rolls[i + 1] + self.rolls[i + 2]
                i += 1
            elif self.rolls[i] + self.rolls[i + 1] == 10:  # spare
                score += 10 + self.rolls[i + 2]
                i += 2
            else:
                score += self.rolls[i] + self.rolls[i + 1]
                i += 2
        return score
