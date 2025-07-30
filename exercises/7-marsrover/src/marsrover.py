#write code here
def jn():
    return 1

class Rover:
    def __init__(self, x: int, y: int, direction: str, map_obj=None):
        # Initialisation minimale pour le premier test
        self.x = x
        self.y = y
        self.direction = direction
        self.map = map_obj # On passera une Map plus tard

    def get_position(self) -> tuple[int, int]:
        return self.x, self.y

    def get_direction(self) -> str:
        return self.direction

# On mettra la classe Map ici plus tard, car le Rover en aura besoin.
class Map:
    def __init__(self, map_string: str = ""):
        self.grid = []
        # Plus tard, on parsera la map_string ici
        pass
