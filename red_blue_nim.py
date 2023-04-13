import sys

# This function evaluates the current state of the game based on the number of red and blue marbles
def evaluate_game_state(num_red, num_blue):
    return 2*num_red + 3*num_blue

# This function gets the human player's move and validates it
def get_human_move(num_red, num_blue):
    while True:
        # Display the current state of the game
        print(f"\nRed: {num_red}, Blue: {num_blue}")

        # Check if the game has ended
        if(num_red == 0) or (num_blue == 0):
            print("Human wins!")
            pile = "red" 
            num = 1
            break
        else:
            # Ask the human player for their move
            pile = input("\nYour turn: ")
            
            # Validate the input
            if pile not in ["red", "blue"]:
                print("Invalid pile!")
                continue
            num = 1
            if pile == "red" and num > num_red:
                print("Not enough red marbles!")
                continue
            if pile == "blue" and num > num_blue:
                print("Not enough blue marbles!")
                continue
            break
    return pile, num

def get_computer_move(num_red, num_blue, max_depth, alpha=float("-inf"), beta=float("inf"), is_max_player=True):
    # Check if either pile is empty
    if num_red == 0 or num_blue == 0:
        # Return a score based on the current game state
        return -evaluate_game_state(num_red, num_blue)

    # Check if maximum depth has been reached
    if max_depth == 0:
        # Return a score based on the current game state
        return evaluate_game_state(num_red, num_blue)

    # Determine whether it is the max player's turn
    if is_max_player:
        # Initialize variables to keep track of the best move found so far
        best_value = float("-inf")
        best_pile = None
        best_num = None

        # Iterate through all possible moves
        for pile, num in [("red", 1), ("blue", 1)]:
            # Check if the move is valid
            if (pile == "red" and num > num_red) or (pile == "blue" and num > num_blue):
                continue

            # Calculate the new number of marbles in each pile after the move
            new_num_red = num_red - (num if pile == "red" else 0)
            new_num_blue = num_blue - (num if pile == "blue" else 0)

            # Recursively call the function with updated values
            value = get_computer_move(new_num_red, new_num_blue, max_depth-1, alpha, beta, False)

            # Keep track of the best move found so far
            if value > best_value:
                best_value = value
                best_pile = pile
                best_num = num

            # Update alpha value
            alpha = max(alpha, best_value)

            # Check if pruning is possible
            if alpha >= beta:
                break

        # If it is the original function call, print the computer's move
        if max_depth == depth:
            print(f"\nComputer's turn\nComputer removes {best_num} marble from {best_pile} pile.")

        # Return the best value found
        return best_value

    # If it is not the max player's turn
    else:
        # Initialize variable to keep track of the best score found so far
        best_value = float("inf")

        # Iterate through all possible moves
        for pile, num in [("red", 1), ("blue", 1)]:
            # Check if the move is valid
            if (pile == "red" and num > num_red) or (pile == "blue" and num > num_blue):
                continue

            # Calculate the new number of marbles in each pile after the move
            new_num_red = num_red - (num if pile == "red" else 0)
            new_num_blue = num_blue - (num if pile == "blue" else 0)

            # Recursively call the function with updated values
            value = get_computer_move(new_num_red, new_num_blue, max_depth-1, alpha, beta, True)

            # Keep track of the best score found so far
            best_value = min(best_value, value)

            # Update beta value
            beta = min(beta, best_value)

            # Check if pruning is possible
            if alpha >= beta:
                break

        # Return the best score found
        return best_value


def red_blue_nim(num_red, num_blue, first_player, depth):
    # Check who is the first player and set is_max_player accordingly
    if first_player == "computer":
        is_max_player = True
    elif first_player == "human":
        is_max_player = False
    else:
        # Print an error message if first_player is neither "computer" nor "human"
        print("Invalid first player!")
        return

    # Start the game loop
    while True:
        # Check if one of the piles is empty, which means the game is over
        if num_red == 0 or num_blue == 0:
            if is_max_player:
                # If the computer is the max player, it wins and gets a score
                print(f"\nRed: {num_red}, Blue: {num_blue}")
                print("\nComputer wins!")
                if num_red == 0:
                    score = 3*num_blue
                else:
                    score = 2*num_red
                print(f"Computer's score: {score}")
                break
            else:
                # If the human is the max player, they win and get a score
                print(f"\nRed: {num_red}, Blue: {num_blue}")
                print("\nYou win!")
                if num_red == 0:
                    score = 3*num_blue
                else:
                    score = 2*num_red
                print(f"Your score: {score}")
                break
        # If the game is not over, make a move
        if is_max_player:
            # If it's the computer's turn, use the get_computer_move function to choose the best move
            print(f"\nRed: {num_red}, Blue: {num_blue}")
            best_value = float("-inf")
            best_pile = None
            best_num = None
            for pile, num in [("red", 1), ("blue", 1)]:
                # Check if the move is valid (i.e. there are enough marbles in the pile)
                if (pile == "red" and num > num_red) or (pile == "blue" and num > num_blue):
                    continue
                new_num_red = num_red - (num if pile == "red" else 0)
                new_num_blue = num_blue - (num if pile == "blue" else 0)
                # Use the get_computer_move function to evaluate the move and get its value
                value = get_computer_move(new_num_red, new_num_blue, 12, is_max_player=is_max_player)
                # If the move has a higher value than the previous best move, update the best move
                if value > best_value:
                    best_value = value
                    best_pile = pile
                    best_num = num
            # Make the best move and update the piles
            new_num_red = num_red - (best_num if best_pile == "red" else 0)
            new_num_blue = num_blue - (best_num if best_pile == "blue" else 0)
            print(f"\nComputer's turn\nComputer removes {best_num} marble from {best_pile} pile.")
        else:
            # If it's the human's turn, use the get_human_move function to get the move from the user
            pile, num = get_human_move(num_red, num_blue)
            # Make the move and update the piles
            new_num_red = num_red - (num if pile == "red" else 0)
            new_num_blue = num_blue - (num if pile == "blue" else 0)
            print(f"You removed {num} marble from {pile} pile.")
        #Finally, num_red and num_blue are updated with the new values and the turn is switched to 
        #the other player by negating the value of is_max_player.
        num_red = new_num_red
        num_blue = new_num_blue
        is_max_player = not is_max_player


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"\nUsage: <file-name.py> <num-red> <num-blue> <first-player> <depth>(depth is optional)")
    else:
        print("\nWelcome to the Modified Red-Blue Nim!")
        print("Enter red or blue to select a pile, and 1 marble will be removed from that pile.")
        num_red = int(sys.argv[1])
        num_blue = int(sys.argv[2])
        if len(sys.argv) >= 4:
            if sys.argv[3] == "computer":
                first_player = "computer"
            elif sys.argv[3] == "human":
                first_player = "human"
            else:
                print("Invalid first player! It should be either 'computer' or 'human'")
                exit()
        else:
            first_player = "computer"
        if len(sys.argv) >= 5:
            depth = int(sys.argv[4])
        else:
            depth = None
        red_blue_nim(num_red, num_blue, first_player, depth)