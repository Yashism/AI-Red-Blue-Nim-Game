Yash Waghmare
1001845079

Python 3.10.6

Code is structured in one file. The evaluate_game_state function takes the number of red and blue marbles and 
returns the total score of the current game state. The get_human_move function prompts the user player to 
enter their move, checks that the move is valid, and returns the pile and number of marbles to remove.
The get_computer_move function implements the computer's strategy using the minimax algorithm with alpha-beta pruning.
The red_blue_nim function defines the main game loop and alternates turns between the human player and the computer. 
It also handles end-of-game scoring and displays appropriate messages to the players.

I couln't implement the depth limit. I tried to implement it by adding a depth parameter to the minimax function and
passing it to the get_computer_move function. But I couldn't figure out how to increment the depth parameter in the
minimax function. I tried to increment it in the get_computer_move function but it didn't work. I also tried to
implement it by adding a depth parameter to the get_computer_move function and passing it to the minimax function.
But the code works fine for the rest without the depth. For now the depth is set to 3.

Here's an example of how to run the code:
python3 red_blue_nim.py 3 3 human

Basically:
python3 red_blue_nim.py <num of red marbles> <num of blue marbles> <human or computer>

Here's a sample run:
------> python3 red_blue_nim.py 3 3 human

Welcome to the Modified Red-Blue Nim!
Enter red or blue to select a pile, and 1 marble will be removed from that pile.

Red: 3, Blue: 3

Your turn: red
You removed 1 marble from red pile.      

Red: 2, Blue: 3

Computer's turn
Computer removes 1 marble from blue pile.

Red: 2, Blue: 2

Your turn: blue 
You removed 1 marble from blue pile.

Red: 2, Blue: 1

Computer's turn
Computer removes 1 marble from red pile.

Red: 1, Blue: 1

Your turn: red
You removed 1 marble from red pile.

Red: 0, Blue: 1

Computer wins!
Computer's score: 3