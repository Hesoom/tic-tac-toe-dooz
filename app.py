import os


board_list = [" " for _ in range(9)]

def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_win(board, player):
    win_combos = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for combo in win_combos:
        if all(board[i] == player for i in combo):
            return True
    return False

def player_move(board, player):
    clear_screen()
    print_board(board)
    while True:
        try:
            player_choose = int(input(f"It's {player}'s turn\nEnter a number for your case (1 to 9): "))
            if player_choose < 1 or player_choose > 9:
                clear_screen()
                print_board(board)
                print("Invalid number. Choose between 1 and 9.")
    
                continue
            if board[player_choose - 1] != " ":
                clear_screen()
                print_board(board)
                print("That spot is already taken!")
                continue
            break
        except ValueError:
            clear_screen()
            print_board(board)
            print("Please enter a valid number.")

    board[player_choose - 1] = player

def start(board):
    player = "X"
    other_player = "O"

    while True:
        clear_screen()
        print_board(board)
        player_move(board, player)

        if check_win(board, player):
            clear_screen()
            print_board(board)
            print(f"🎉 {player} wins!")
            if play_again():
                board[:] = [" " for _ in range(9)]
                continue
            else:
                print("Goodbye!")
                break
        
        if " " not in board:
            clear_screen()
            print_board(board)
            print("It's a draw!")
            if play_again():
                board = [" " for _ in range(9)]
                continue
            else:
                print("Goodbye!")
                break

        # Switch player
        player, other_player = other_player, player
    
def play_again ():
        # Play again
    while True:
        play = input("Do you want to play again? (y/n): ").lower()
        if play == 'y':
            return True
        elif play == 'n':
            return False
        else:
            print("Please enter a valid answer.")

start(board_list)
