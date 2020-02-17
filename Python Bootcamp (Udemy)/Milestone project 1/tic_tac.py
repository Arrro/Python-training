# 2 players
# 3x3 board going left to right in numbers:
# 789
# 456
# 123
# Prompt player 1 for X or O

board = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
]

def win_lines():
    i = 0
    while i < len(board):
        if board[i] == board[i - 1] and board[i] == board[i - 2]:
            return True
        i += 1
    return False

def display_board():
    print('\n', ' ', board[0], '|', board[1], '|', board[2], '\n', 
        '-------------', '\n',
        ' ', board[3], '|', board[4], '|', board[5],'\n',
        '-------------', '\n',
        ' ', board[6], '|', board[7], '|', board[8], '\n')

def player_select(player_input):
    player_1 = ''
    player_2 = ''
    player_1 += player_input

    if player_1 == 'X':
        player_2 = 'O'
    elif player_1 == 'O':
        player_2 = 'X'

    print(f'Player 1 is {player_1} and Player 2 you are {player_2}')

def play1_choice(choice):
    i = 0
    while i <= len(board):
        if board[i] == choice:
            board[i] = 'X'
            break
        else:
            i += 1

def play2_choice(choice):
    i = 0
    while i <= len(board):
        if board[i] == choice:
            board[i] = 'X'
            break
        else:
            i += 1

print('Welcome to Tic Tac Toe!')
player_input = input("Player #1 do you wish to be X or O: ").upper()
player_select(player_input)
print('Lets begin.')

while win_lines() is False:
    print('Player 1, its your turn: ')
    display_board()
    choice = int(input())
    play1_choice(choice)
    win_lines()
    print('Player 2, its your turn: ')
    display_board()
    choice = int(input())
    play2_choice(choice)
    display_board()
    win_lines()