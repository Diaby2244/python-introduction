import unittest
from src.marsrover import Rover, Map

class TestRoverInitialization(unittest.TestCase):

    def test_rover_initial_position_and_direction(self):
        dummy_map = Map()
        initial_x, initial_y = 0, 0
        initial_direction = 'N'
        rover = Rover(initial_x, initial_y, initial_direction, dummy_map)
        self.assertEqual(rover.get_position(), (initial_x, initial_y))
        self.assertEqual(rover.get_direction(), initial_direction)

    def test_rover_moves_forward_facing_north(self):
        map_data = """
🟩🟩🟩
🟩🟩🟩
🟩🟩🟩
"""
        map_obj = Map(map_data)
        rover = Rover(1, 1, 'N', map_obj)
        rover.execute('⬆️')
        self.assertEqual(rover.get_position(), (1, 0))  #
