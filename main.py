import random   

# Step 1: Create the board
board = [" " for _ in range(9)]  # 9 empty spaces (1D list)

def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")


    


# Test printing
def player_move():
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit():  # check if input is a number
            move = int(move) - 1  # adjust to list index (0–8)
            if 0 <= move <= 8 and board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Invalid move, spot already taken or out of range.")
        else:
            print("Please enter a valid number between 1 and 9.")

# Test it

# player_move()
# print_board()


def is_winner(player):
    # All possible winning combinations
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    
    for combo in win_conditions:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False


def minimax(board, depth, is_maximizing):
    # Base cases
    if is_winner("O"):
        return 10 - depth     # AI win -> positive (prefer earlier wins)
    if is_winner("X"):
        return depth - 10    # Human win -> negative (prefer later losses)
    if " " not in board:
        return 0             # Draw

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"                      # try move
                score = minimax(board, depth+1, False)
                board[i] = " "                      # undo move
                if score > best_score:
                    best_score = score
        return best_score
    else:  # minimizing (human)
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth+1, True)
                board[i] = " "
                if score < best_score:
                    best_score = score
        return best_score





def ai_move():
    best_score = -float("inf")
    best_moves = []

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)  # after AI move, it's human's turn
            board[i] = " "
            if score > best_score:
                best_score = score
                best_moves = [i]
            elif score == best_score:
                best_moves.append(i)

    # pick randomly among equally-good moves
    if best_moves:
        move = random.choice(best_moves)
        board[move] = "O"


while True:
    print_board()
    player_move()

    if is_winner("X"):
        print_board()
        print("Player X wins!!")
        break
    if " "not in board:
        print_board()
        print("TIE!")
        break
    ai_move()

    if is_winner("O"):
        print_board()
        print("AI (O) won!")
        break
   
    





# print_board()
# player_move()
# print_board()

