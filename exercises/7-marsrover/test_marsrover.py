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
