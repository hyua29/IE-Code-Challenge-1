import unittest
from test import support

from pacman import *


class PacmanGameTestCases(unittest.TestCase):
    def setUp(self):
        self.game = PacmanGame()
        return super().setUp()
    
    def test_perform_place(self):
        # position pacman
        self.game.pacman_x = 1
        self.game.pacman_y = 2
        self.game.pacman_direction = SOUTH

        command = "PLACE 0,0,NORTH"
        self.game.perform_place(command)

        self.assertEquals(self.game.pacman_x, 0)
        self.assertEquals(self.game.pacman_y, 0)
        self.assertEquals(self.game.pacman_direction, NORTH)
        
    def test_perform_place_wont_fall(self):
        # position pacman
        self.game.pacman_x = 1
        self.game.pacman_y = 2
        self.game.pacman_direction = SOUTH

        command = "PLACE -1,5,NORTH"
        self.game.perform_place(command)

        self.assertEquals(self.game.pacman_x, 1)
        self.assertEquals(self.game.pacman_y, 2)
        self.assertEquals(self.game.pacman_direction, SOUTH)
        
    def test_perform_move_east(self):
        command = "PLACE 1,1,EAST"
        self.game.perform_place(command)
        self.game.perform_move()
        
        self.assertEquals(self.game.pacman_x, 2)
        self.assertEquals(self.game.pacman_y, 1)
    
    def test_perform_move_north(self):
        command = "PLACE 1,1,NORTH"
        self.game.perform_place(command)
        self.game.perform_move()
        
        self.assertEquals(self.game.pacman_x, 1)
        self.assertEquals(self.game.pacman_y, 2)
        
    def test_perform_move_south(self):
        command = "PLACE 1,1,EAST"
        self.game.perform_place(command)
        self.game.perform_move()
        
        self.assertEquals(self.game.pacman_x, 2)
        self.assertEquals(self.game.pacman_y, 1)
                
    def test_perform_move_west(self):
        command = "PLACE 1,1,WEST"
        self.game.perform_place(command)
        self.game.perform_move()
        
        self.assertEquals(self.game.pacman_x, 0)
        self.assertEquals(self.game.pacman_y, 1)
        
    def test_perform_move_wont_fall(self):
        command = "PLACE 0,0,WEST"
        self.game.perform_place(command)
        self.game.perform_move()
        
        self.assertEquals(self.game.pacman_x, 0)
        self.assertEquals(self.game.pacman_y, 0)
        
    def test_perform_report(self):
        command = "PLACE 0,0,WEST"
        self.game.perform_place(command)

        report = self.game.perform_report()
        expected_report = "0,0,WEST"

        self.assertEquals(report, expected_report)
    
    def test_run_command_invalid_command_raise_error(self):
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