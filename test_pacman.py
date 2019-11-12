import unittest
from test import support

from pacman import *


class PacmanGameTestCases(unittest.TestCase):
    def setUp(self):
        self.game = PacmanGame()
        return super().setUp()
    
    def test_perform_place(self):
        self.game.pacman_x = 1
        self.game.pacman_y = 2
        self.game.pacman_direction = SOUTH

        command = "PLACE 0,0,NORTH"
        self.game.perform_place(command)

        # pacman positioned successfully
        self.assertEquals(self.game.pacman_x, 0)
        self.assertEquals(self.game.pacman_y, 0)
        self.assertEquals(self.game.pacman_direction, NORTH)
        
    def test_perform_place_wont_fall(self):
        self.game.pacman_x = 1
        self.game.pacman_y = 2
        self.game.pacman_direction = SOUTH

        command = "PLACE -1,5,NORTH"
        self.game.perform_place(command)

        # position should not change
        self.assertEquals(self.game.pacman_x, 1)
        self.assertEquals(self.game.pacman_y, 2)
        self.assertEquals(self.game.pacman_direction, SOUTH)
        
    def test_perform_move_east(self):
        self.game.pacman_x = 1
        self.game.pacman_y = 1
        self.game.pacman_direction = EAST

        self.game.perform_move()
        
        # has moved to right position
        self.assertEquals(self.game.pacman_x, 2)
        self.assertEquals(self.game.pacman_y, 1)
    
    def test_perform_move_north(self):
        self.game.pacman_x = 1
        self.game.pacman_y = 1
        self.game.pacman_direction = NORTH

        self.game.perform_move()
        
        # has moved to right position
        self.assertEquals(self.game.pacman_x, 1)
        self.assertEquals(self.game.pacman_y, 2)
        
    def test_perform_move_south(self):
        self.game.pacman_x = 1
        self.game.pacman_y = 1
        self.game.pacman_direction = EAST

        self.game.perform_move()

        # has moved to right position
        self.assertEquals(self.game.pacman_x, 2)
        self.assertEquals(self.game.pacman_y, 1)
                
    def test_perform_move_west(self):
        self.game.pacman_x = 1
        self.game.pacman_y = 1
        self.game.pacman_direction = WEST

        self.game.perform_move()
        
        # has moved to right position
        self.assertEquals(self.game.pacman_x, 0)
        self.assertEquals(self.game.pacman_y, 1)
        
    def test_perform_move_wont_fall(self):
        self.game.pacman_x = 0
        self.game.pacman_y = 0
        self.game.pacman_direction = WEST

        self.game.perform_move()

        # has moved to right position
        self.assertEquals(self.game.pacman_x, 0)
        self.assertEquals(self.game.pacman_y, 0)
        
    def test_perform_report(self):
        self.game.pacman_x = 0
        self.game.pacman_y = 0
        self.game.pacman_direction = WEST

        report = self.game.perform_report()
        expected_report = "0,0,WEST"

        # Right report for current position
        self.assertEquals(report, expected_report)
    
    def test_run_command_raise_error_if_invalid_command(self):
        self.assertRaises(ValueError, self.game.run_command("INVALID"))
        
    def test_pacman_game_1(self):
        self.game.run_game("test_input_a.txt")

        report = self.game.perform_report()
        expected_report = "0,1,NORTH"

        self.assertEquals(report, expected_report)
        
    def test_pacman_game_1(self):
        self.game.run_game("test_input_b.txt")

        report = self.game.perform_report()
        expected_report = "0,0,WEST"

        self.assertEquals(report, expected_report)
        
    def test_pacman_game_1(self):
        self.game.run_game("test_input_c.txt")

        report = self.game.perform_report()
        expected_report = "3,3,NORTH"

        self.assertEquals(report, expected_report)

        
if __name__ == '__main__':
    support.run_unittest(PacmanGameTestCases)