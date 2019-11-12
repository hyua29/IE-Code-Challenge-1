Pacman Simulator
===

Thank you for taking your time to review the code.

The code is written without any third party libraries, so it should be able to run so long as **python3 (3.7.2)** is in place. However, please use **pipenv** to activate the software environment if any setup error occurs.

The code is written under the assumption that **all input commands are in valid format**.

#### Run Simulator
The source code of the simulator is under pacman.py. run_game() takes in the path of an input file and runs all the instructions inside.
```
game = PacmanGame()
game.run_game("input.txt")
```

#### Run Tests

test_pacman.py is provided to verify the correctness of the simulator.

To run the tests, please run the following command in the shell under the root folder.
```
python3 test_pacman.py 
```

#### Activate pipenv

Install pipenv.

Run the following command in the shell under the root folder.
```
pipenv shell
```



