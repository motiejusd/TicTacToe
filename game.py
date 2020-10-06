# simple tic-tac-toe game

game_board = {7: ' ', 8: ' ', 9: ' ',
              4: ' ', 5: ' ', 6: ' ',
              1: ' ', 2: ' ', 3: ' '}


def print_board(board):
    print(f"|{board[7]}|{board[8]}|{board[9]}|\n"
          f"|{board[4]}|{board[5]}|{board[6]}|\n"
          f"|{board[1]}|{board[2]}|{board[3]}|\n")


def game():
    player = 'X'
    moves = 0
    win = False
    tie = False

    while moves < 9:

        print_board(game_board)
        placement = int(input(f"Make your move, {player}"))

        if game_board[placement] != ' ':
            print("Illegal move.")
        else:
            game_board[placement] = player
            moves += 1

            if moves >= 5:
                if game_board[7] == game_board[5] and game_board[7] == game_board[3]:
                    win = True
                elif game_board[1] == game_board[5] and game_board[1] == game_board[9]:
                    win = True
                elif game_board[7] == game_board[8] and game_board[7] == game_board[9]:
                    win = True
                elif game_board[4] == game_board[5] and game_board[4] == game_board[6]:
                    win = True
                elif game_board[1] == game_board[2] and game_board[1] == game_board[3]:
                    win = True
                elif game_board[7] == game_board[4] and game_board[7] == game_board[1]:
                    win = True
                elif game_board[8] == game_board[5] and game_board[8] == game_board[2]:
                    win = True
                elif game_board[9] == game_board[6] and game_board[9] == game_board[3]:
                    win = True

                if moves == 9 and not win:
                    print_board(game_board)
                    print(f"Game over. It's a tie.")
                    break
                if win:
                    print_board(game_board)
                    print(f"Game over. Player {player} won.")
                    break

            if player == 'X':
                player = 'O'
            else:
                player = 'X'


game()
# print_board(game_board)
