# 2 players
# 3x3 board going left to right in numbers:
# 789
# 456
# 123
# Prompt player 1 for X or O

board = [
    1 ,'|', 2, '|', 3,
    4, '|', 5, '|', 6,
    7 ,'|', 8 ,'|', 9
]

win = False
win1 = board[1] and board[2] and board[3] == 'X' or 'O'
win2 = board[4] and board[5] and board[6] == 'X' or 'O'
win3 = board[7] and board[8] and board[9] == 'X' or 'O'
win4 = board[1] and board[5] and board[9] == 'X' or 'O'
win5 = board[7] and board[5] and board[3] == 'X' or 'O'

def display_board():
    print('\n', ' ', board[0], board[1], board[2], board[3], board[4], '\n', 
        '-------------', '\n',
        ' ', board[5], board[6], board[7], board[8], board[9],'\n',
        '-------------', '\n',
        ' ', board[10], board[11], board[12], board[13], board[14], '\n')

def player_select(player_input):
    player_1 = ''
    player_2 = ''
    player_1 += player_input

    if player_1 == 'X':
        player_2 = 'O'
    elif player_1 == 'O':
        player_2 = 'X'

    print(f'Player 1 is {player_1} and Player 2 you are {player_2}')

def play_choice(choice):
    i = 0

    while i <= len(board):
        if board[i] == choice:
            board[i] = 'X'
            break
        elif board[i] == 'X' or 'O':
            print('Slot is already chosen!')
            break

print('Welcome to Tic Tac Toe!')
player_input = input("Player #1 do you wish to be X or O: ").upper()
player_select(player_input)
print('Lets begin.')

while win is False:
    print('Player 1, its your turn: ')
    display_board()
    choice = int(input())
    play_choice(choice)
    print('Player 2, its your turn: ')
    display_board()
    choice = int(input())
    play_choice(choice)

    break
