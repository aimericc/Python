#/usr/bin/env python
# coding: utf-8

# In[1]:


def display_board(board):
    board_list = board
    return board_list


# In[2]:


def player_mark_func():
    active = True

    while active:
        player_mark_prefer = input(
            "Player 1, you want go first(X) or last(O)? ")

        if player_mark_prefer in ['first', 'X']:
            player_mark_temp = 'X'
            active = False
        elif player_mark_prefer in ['last', 'O']:
            player_mark_temp = 'O'
            active = False
        elif player_mark_prefer.lower() == 'quit':
            print("Session interrupted by user.")
            player_mark_temp = 0
            active = False
        else:
            print("Enter 'first', 'last', 'O' or 'X': ")
            active = True

    return player_mark_temp


# In[3]:


def player_input():
    while True:
        player_input_position = input("Enter the position (1-9): ")
        if player_input_position.isdigit():
            if int(player_input_position) not in range(1, 10):
                print("Enter again(1-9): ")
            elif not space_check(test_board, int(player_input_position)):
                print("Space already filled, Enter again(1-9): ")
            else:
                return int(player_input_position)
        elif player_input_position.lower() == 'quit':
            print("Session interrupted by user.")
            break
        else:
            print("cannot recognize, Enter again(1-9): ")


# In[4]:


def place_marker(board, marker, position):
    board[position - 1] = marker


# In[5]:


def win_check(board, mark):
    mark_win_check = mark
    if board[0] == mark_win_check:
        if board[1] == mark_win_check:
            if board[2] == mark_win_check:
                return True
        elif board[3] == mark_win_check:
            if board[6] == mark_win_check:
                return True
        elif board[4] == mark_win_check:
            if board[8] == mark_win_check:
                return True
    elif board[1] == mark_win_check:
        if board[4] == mark_win_check:
            if board[7] == mark_win_check:
                return True
    elif board[2] == mark_win_check:
        if board[5] == mark_win_check:
            if board[8] == mark_win_check:
                return True
        elif board[4] == mark_win_check:
            if board[6] == mark_win_check:
                return True
    elif board[3] == mark_win_check:
        if board[4] == mark_win_check:
            if board[5] == mark_win_check:
                return True
    elif board[6] == mark_win_check:
        if board[7] == mark_win_check:
            if board[8] == mark_win_check:
                return True
    else:
        return False


# In[6]:


def space_check(board, position):
    if board[position - 1] != '':
        return False
    else:
        return True


# In[7]:


def full_board_check(board):
    for i in board:
        if i == '':
            return False
    return True


# In[8]:


def replay():
    replay_prefer = input("GAME OVER!! Do you want to play again?(Y/N) ")
    if replay_prefer.upper() == 'Y':
        return True
    else:
        return False


# In[10]:


print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    test_board = ['', '', '', '', '', '', '', '', '']
    display_board(test_board)

    # player_mark = ''
    # while player_mark not in ['X', 'O', 'first', 'last']:
    player_mark = player_mark_func()

    while True:
        # Player 1 Turn
        player_input_num = player_input()

        place_marker(test_board, player_mark, player_input_num)
        display_board(test_board)

        if win_check(test_board, player_mark):
            if player_mark == 'O':
                print("O player wins!!")
                # replay()
                break
            elif player_mark == 'X':
                print("X player wins!!")
                # replay()
                break
        elif full_board_check(test_board):
            print("Space is full, no body wins!")
            # replay
            break
        else:
            if player_mark == 'O':
                player_mark = 'X'
            else:
                player_mark = 'O'
            continue

    if not replay():
        break


# In[ ]:




