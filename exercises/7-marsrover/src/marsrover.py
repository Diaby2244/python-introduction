class Rover:
    def __init__(self, x: int, y: int, direction: str, map_obj=None):
        self.x = x
        self.y = y
        self.direction = direction
        self.map = map_obj

    def get_position(self) -> tuple[int, int]:
        return self.x, self.y

    def get_direction(self) -> str:
        return self.direction

    def execute(self, command: str):
        if command == '➡️':
            self.direction = {
                'N': 'E',
                'E': 'S',
                'S': 'W',
                'W': 'N'
            }[self.direction]

        elif command == '⬅️':
            self.direction = {
                'N': 'W',
                'W': 'S',
                'S': 'E',
                'E': 'N'
            }[self.direction]

        elif command == '⬆️':
            if self.direction == 'N':
                new_x, new_y = self.x, self.y - 1
            elif self.direction == 'S':
                new_x, new_y = self.x, self.y + 1
            elif self.direction == 'E':
                new_x, new_y = self.x + 1, self.y
            elif self.direction == 'W':
                new_x, new_y = self.x - 1, self.y
            else:
                return

            if (
                0 <= new_x < self.map.width
                and 0 <= new_y < self.map.height
                and self.map.grid[new_y][new_x] != '🌳'
            ):
                self.x = new_x
                self.y = new_y


class Map:
    def __init__(self, map_string: str = ""):
        self.grid = []
        if map_string:
            lines = map_string.strip().split('\n')
            for line in lines:
                self.grid.append(list(line.strip()))
        self.height = len(self.grid)
        self.width = len(self.grid[0]) if self.grid else 0

    def execute(self, command: str):
        if command == '➡️':
            self.direction = {
                'N': 'E',
                'E': 'S',
                'S': 'W',
                'W': 'N'
            }[self.direction]

        elif command == '⬅️':
            self.direction = {
                'N': 'W',
                'W': 'S',
                'S': 'E',
                'E': 'N'
            }[self.direction]

        elif command == '⬆️':
            if self.direction == 'N':
                new_x, new_y = self.x, self.y - 1
            elif self.direction == 'S':
                new_x, new_y = self.x, self.y + 1
            elif self.direction == 'E':
                new_x, new_y = self.x + 1, self.y
            elif self.direction == 'W':
                new_x, new_y = self.x - 1, self.y
            else:
                return

            if (
                    0 <= new_x < self.map.width
                    and 0 <= new_y < self.map.height
                    and self.map.grid[new_y][new_x] != '🌳'
            ):
                self.x = new_x
                self.y = new_y
