import unittest
from src.marsrover import Rover, Map

class TestRoverInitialization(unittest.TestCase):

    def test_rover_initial_position_and_direction(self):
        dummy_map = Map()
        rover = Rover(0, 0, 'N', dummy_map)
        self.assertEqual(rover.get_position(), (0, 0))
        self.assertEqual(rover.get_direction(), 'N')

    def test_rover_moves_forward_facing_north(self):
        map_data = """
🟩🟩🟩
🟩🟩🟩
🟩🟩🟩
"""
        map_obj = Map(map_data)
        rover = Rover(1, 1, 'N', map_obj)
        rover.execute('⬆️')
        self.assertEqual(rover.get_position(), (1, 0))

    def test_rover_turns_right(self):
        dummy_map = Map()
        rover = Rover(0, 0, 'N', dummy_map)

        rover.execute('➡️')
        self.assertEqual(rover.get_direction(), 'E')

        rover.execute('➡️')
        self.assertEqual(rover.get_direction(), 'S')

        rover.execute('➡️')
        self.assertEqual(rover.get_direction(), 'W')

        rover.execute('➡️')
        self.assertEqual(rover.get_direction(), 'N')

    def test_rover_turns_left(self):
        dummy_map = Map()
        rover = Rover(0, 0, 'N', dummy_map)

        rover.execute('⬅️')
        self.assertEqual(rover.get_direction(), 'W')

        rover.execute('⬅️')
        self.assertEqual(rover.get_direction(), 'S')

        rover.execute('⬅️')
        self.assertEqual(rover.get_direction(), 'E')

        rover.execute('⬅️')
        self.assertEqual(rover.get_direction(), 'N')

    def test_rover_does_not_move_into_obstacle(self):
        map_data = """
    🟩🟩🟩
    🟩🌳🟩
    🟩🟩🟩
    """
        map_obj = Map(map_data)
        rover = Rover(1, 2, 'N', map_obj)  # Position en (1, 2), face nord

        rover.execute('⬆️')  # La case au nord (1,1) est un arbre 🌳, donc obstacle

        # Le rover doit rester à la même position
        self.assertEqual(rover.get_position(), (1, 2))

    def test_rover_does_not_enter_water(self):
        map_data = """
    🟩🟩🟩
    🟩💧🟩
    🟩🟩🟩
    """
        map_obj = Map(map_data)
        rover = Rover(1, 2, 'N', map_obj)  # juste sous la case avec 💧
        rover.execute('⬆️')  # essaie d’avancer vers l’eau
        self.assertEqual(rover.get_position(), (1, 2))  # ne bouge pas

    def test_rover_does_not_exit_map_north(self):
        map_data = """
    🟩🟩🟩
    🟩🟩🟩
    🟩🟩🟩
    """
        map_obj = Map(map_data)
        rover = Rover(1, 0, 'N', map_obj)  # tout en haut
        rover.execute('⬆️')  # essaie d’avancer en dehors
        self.assertEqual(rover.get_position(), (1, 0))  # reste à sa place

    def test_rover_turns_left_four_times(self):
        dummy_map = Map()
        rover = Rover(0, 0, 'N', dummy_map)

        rover.execute('⬅️')
        self.assertEqual(rover.get_direction(), 'W')

        rover.execute('⬅️')
        self.assertEqual(rover.get_direction(), 'S')

        rover.execute('⬅️')
        self.assertEqual(rover.get_direction(), 'E')

        rover.execute('⬅️')
        self.assertEqual(rover.get_direction(), 'N')  # retour à la position initiale

    def test_rover_position_and_direction_after_move(self):
        map_data = """ 
    🟩🟩🟩
    🟩🟩🟩
    🟩🟩🟩
    """
        map_obj = Map(map_data)
        rover = Rover(1, 1, 'S', map_obj)

        rover.execute('⬆️')
        rover.execute('➡️')

        self.assertEqual(rover.get_position(), (1, 2))
        self.assertEqual(rover.get_direction(), 'W')

    def test_rover_rotates_twice_then_moves(self):
        map_data = """
    🟩🟩🟩🟩
    🟩🟩🟩🟩
    🟩🟩🟩🟩
    """
        map_obj = Map(map_data)
        rover = Rover(1, 1, 'N', map_obj)

        rover.execute('➡️')  # N -> E
        rover.execute('➡️')  # E -> S
        rover.execute('⬆️')  # avance vers le sud (y + 1)

        self.assertEqual(rover.get_position(), (1, 2))  # y+1
        self.assertEqual(rover.get_direction(), 'S')
