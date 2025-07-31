class Game:
    def __init__(self, rolls: str = ""):
        # Nettoyer la chaîne en supprimant les espaces et convertir en liste de caractères
        self.rolls = [c for c in rolls.replace(" ", "")]
        # Convertir les lancers en valeurs numériques (int) en gérant les spares
        self.values = self._convert_rolls_to_values()

    def _convert_rolls_to_values(self):
        values = []
        for i, c in enumerate(self.rolls):
            if c == 'X':  # Strike
                values.append(10)
            elif c == '-':  # Raté
                values.append(0)
            elif c == '/':  # Spare = 10 moins valeur précédente
                values.append(10 - values[-1])
            else:
                values.append(int(c))
        return values

    def score(self):
        total = 0
        i = 0  # index pour parcourir les lancers en valeurs numériques

        # Calcul des 9 premières frames
        for frame in range(10):
            value = self.values[i]
            if value == 10:  # Strike
                total += 10 + self.values[i + 1] + self.values[i + 2]
                i += 1
            elif value + self.values[i + 1] == 10:  # Spare
                total += 10 + self.values[i + 2]
                i += 2
            else:  # Open frame
                total += value + self.values[i + 1]
                i += 2

        return total
