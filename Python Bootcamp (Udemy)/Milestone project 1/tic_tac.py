# 2 players
# 3x3 board going left to right in numbers:
# 789
# 456
# 123
# Prompt player 1 for X or O

board = [
    7 ,'|', 8, '|', 9, '|','\n',
    4, '|', 5, '|', 6 ,'|','\n',
    1 ,'|', 2 ,'|', 3, '|'
]


win = False
win1 = board[1] and board[2] and board[3] == 'X' or 'O'
win2 = board[4] and board[5] and board[6] == 'X' or 'O'
win3 = board[7] and board[8] and board[9] == 'X' or 'O'
win4 = board[1] and board[5] and board[9] == 'X' or 'O'
win5 = board[7] and board[5] and board[3] == 'X' or 'O'

#def display_board():
print('\n', ' ', board[1], board[3], board[5],'\n', '---------', board[6], ' ', board[8], board[10], board[12],'\n','---------', board[13], ' ', board[15], board[17], board[19])

def player_choice():
    pass

def player_select():
    player_1 = ''
    player_2 = ''
    player_input = input("Player #1 do you wish to be X or O: ")
    if player_input == 'X':
        player_1 == 'X'
    else:
        player_2 == 'O'

while win is False:
    print('Welcome to Tic Tac Toe!')
    print('\n', ' ', board[1], board[3], board[5],'\n', '---------', board[6], ' ', board[8], board[10], board[12],'\n','---------', board[13], ' ', board[15], board[17], board[19])
    player_select()