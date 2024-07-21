from IPython.display import clear_output
import random

def display_board(board):
    
    print('   |   |   ')
    print(f' {board[7]} | {board[8]} | {board[9]} ')
    print('___|___|___')
    print('   |   |   ')
    print(f' {board[4]} | {board[5]} | {board[6]} ')
    print('___|___|___')
    print('   |   |   ')
    print(f' {board[1]} | {board[2]} | {board[3]} ')
    print('   |   |   ')

def player_input():
    choice='wrong'
    while choice not in ['X','O']:
        choice=input("Please pick a marker for Player 1: 'X' or 'O': ")
        if choice not in ['X','O']:
            print("Please pick a valid value")
    return choice  

def place_marker(board, marker, position):
    board[position]=marker
    return board

def win_check(board, mark):  

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
        (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
        (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
        (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
        (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
        (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
        (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
        (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


def choose_first():
    player=random.randint(1,2)
    if player==1:
        print("Player 1 goes first")
        return "Player 1"
    else:    
        print("Player 2 goes first")
        return "Player 2"

def space_check(board, position):
    
    if board[position]==' ':
        return True
    else:
        return False


def full_board_check(board):
    num=0
    for x in board:
        if x=='X' or x=='O':
            num+=1
    if num==9:
        return True
    return False  

def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

def replay():
    choice='wrong'
    while choice not in ['Y','N']:
        choice=input("Do you want to play again (Y/N): ")
        if choice not in ['Y','N']:
            clear_output()
            print("Pick between Y and N")
    if choice=='Y':
        return True
    return False  

print('Welcome to Tic Tac Toe!')

#while True:
    # Set the game up here
    #pass

    #while game_on:
        #Player 1 Turn
        
        
        # Player2's turn.
            
            #pass

    #if not replay():
        #break

board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
playon=True
while True:
    player1=player_input()
    player2=''
    if player1=='X':
        player2='O'
    else:
        player2='X'
    m1={"Player 1":player1,"Player 2":player2}    
    turn=choose_first()
    print("Turn: "+turn)
    while playon:
        print("Turn: "+turn)
        if turn=='Player 1':
            print("Player 1")
            display_board(board)
            position=player_choice(board)
            board=place_marker(board,player1,position)
            display_board(board)  
            if win_check(board, player1):
                print("Congratulations Player 1 won the game")
                display_board(board)
                playon = False
            else:
                if full_board_check(board):
                    print("Tie")
                    display_board(board)
                    break
                else:
                    turn='Player 2'
        else:
            print("Player 2")
            display_board(board)
            position=player_choice(board)
            board=place_marker(board,player2,position)
            display_board(board)
            if win_check(board, player2):
                print("Congratulations Player 2 won the game")
                display_board(board)
                playon = False
            else:
                if full_board_check(board):
                    print("Tie")
                    display_board(board)
                    break
                else:
                    turn='Player 1'

    if not replay():
        print("Game ended")
        break

