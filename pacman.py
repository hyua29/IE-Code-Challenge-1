# Commands
PLACE  = 'PLACE'
LEFT = 'LEFT'
RIGHT = 'RIGHT'
MOVE = 'MOVE'
REPORT = 'REPORT'

# Pacman directions
NORTH = 'NORTH'
SOUTH = 'SOUTH'
WEST = 'WEST'
EAST = 'EAST'

# Grid dimensions
GRID_WIDTH = 5
GRID_HEIGHT = 5


class PacmanGame:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pacman_direction = None
        self.pacman_x = -1
        self.pacman_y = -1
        
    def run_game(self, input_filepath):
        commands = self.read_commands(input_filepath)
        for command in commands:
            self.run_command(command)
            
    def read_commands(self, input_filepath):
        lines = open(input_filepath, "r").readlines()
        commands = [line.rstrip("\n\r") for line in lines]
        return commands

    def run_command(self, command):
        if command == '':
            return
        if self.pacman_direction is None and not PLACE in command: # The first command must be PLACE
            return

        # run commands accordingly
        if PLACE in command:
            self.perform_place(command)
        elif LEFT in command:
            self.perform_left()
        elif RIGHT in command:
            self.perform_right()
        elif MOVE in command:
            self.perform_move()
        elif REPORT in command:
            self.perform_report()
        else:
            raise ValueError("Invalid command: {}".format(command))

    def perform_place(self, command):
        detailed_command = command.split()
        position_details = detailed_command[1].split(',')
        
        x = int(position_details[0])
        y = int(position_details[1])
        new_direction = position_details[2]

        if not self.is_out_of_range(x, y): # update pacman position only if it's a valid location
            self.pacman_x = x
            self.pacman_y = y
            self.pacman_direction = new_direction

    def perform_left(self):
        if self.pacman_direction is None:
            return

        if self.pacman_direction == NORTH:
            self.pacman_direction = WEST
        if self.pacman_direction == WEST:
            self.pacman_direction = SOUTH
        if self.pacman_direction == SOUTH:
            self.pacman_direction = EAST
        if self.pacman_direction == EAST:
            self.pacman_direction =NORTH

    def perform_right(self):
        if self.pacman_direction is None:
            return

        if self.pacman_direction == NORTH:
            self.pacman_direction = EAST
        if self.pacman_direction == EAST:
            self.pacman_direction = SOUTH
        if self.pacman_direction == SOUTH:
            self.pacman_direction = WEST
        if self.pacman_direction == WEST:
            self.pacman_direction = NORTH

    def perform_move(self):
        if self.pacman_direction is None:
            return
        
        if self.pacman_direction == NORTH:
            next_x = self.pacman_x
            next_y = self.pacman_y + 1
        if self.pacman_direction == EAST:
            next_x = self.pacman_x + 1
            next_y = self.pacman_y
        if self.pacman_direction == SOUTH:
            next_x = self.pacman_x
            next_y = self.pacman_y - 1
        if self.pacman_direction == WEST:
            next_x = self.pacman_x - 1
            next_y = self.pacman_y
        
        if not self.is_out_of_range(next_x, next_y):
            self.pacman_x = next_x
            self.pacman_y = next_y
        
    def perform_report(self):
        report = "{},{},{}".format(self.pacman_x, self.pacman_y, self.pacman_direction)
        print(report)
        return report

    def is_out_of_range(self, new_x, new_y):
        if new_x >= GRID_WIDTH or new_x < 0 or new_y >= GRID_HEIGHT or new_y < 0:
            return True
        return False

# example run
if __name__ == "__main__":
    game = PacmanGame()
    game.run_game("input.txt")