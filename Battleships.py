from random import randint
# this is a battleship game i developed in python while learning the language at HyperionDev bootcamp
# the game is a simple version of the classic battleship game to play in the terminal
# the game is played by guessing the row and column of the battleship                                   
# the game is won if the battleship is guessed in 4 turns



board = []
row_names = ["A", "B", "C", "D", "E"]

for x in range(5):
    board.append(["O"] * 5)
# this defines the board as a 5x5 grid
def print_board(board):
    print("  1  2  3  4  5")
    for idx, row in enumerate(board):
        print("{} {}".format(row_names[idx], "  ".join(row)))
        if idx < 4:
            print("  -  -  -  -  -")

print("Let's play Battleship!")
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

# this defines the random row and column functions

ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row)
print(ship_col)

# this defines the battleship location as a random row and column
# this for loop is the game loop deciding the number of turns
for turn in range(4):
    print("Turn", turn + 1)
    guess_row = row_names.index(input("Guess Row: ").upper())
    guess_col = int(input("Guess Col: ")) - 1

# this if statement is the game logic and for user input
    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sank my battleship!")
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print("Oops, that's not even in the ocean.")
        elif(board[guess_row][guess_col] == "X"):
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
        print_board(board)
        if (turn == 3):
            print("Game Over")
"""
# creating dictionary called leadrboard
leaderboard = {}
# creating a function to add a new player to the leaderboard
def add_player():
    name = input("Enter your name: ")
    score = int(input("Enter your score: "))
    leaderboard[name] = score
    # and a function to udpate the score of an existing player
def update_score():
    name = input("Enter your name: ")
    score = int(input("Enter your score: "))
    if name in leaderboard:
        if leaderboard[name] < score:
            leaderboard[name] = score
    else:
        print("Player not found")
"""