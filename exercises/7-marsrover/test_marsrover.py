# test_marsrover.py
import unittest
# Importe la classe Rover depuis le module marsrover dans le package src
from src.marsrover import Rover, Map


class TestRoverInitialization(unittest.TestCase):

    def test_rover_initial_position_and_direction(self):
        # Crée une instance de Map, même vide, car le Rover en a besoin dans son __init__
        dummy_map = Map()

        # Initialise le Rover à une position (0,0) et une direction 'N' (Nord)
        initial_x, initial_y = 0, 0
        initial_direction = 'N'
        rover = Rover(initial_x, initial_y, initial_direction, dummy_map)

        # Vérifie que la position et la direction du Rover sont celles qui ont été définies
        self.assertEqual(rover.get_position(), (initial_x, initial_y))
        self.assertEqual(rover.get_direction(), initial_direction)


