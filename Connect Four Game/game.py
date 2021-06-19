from pprint import pprint


def create_matrix():
    matrix = []
    for i in range(6):
        matrix.append([0] * 7)
    return matrix


def validation(n):
    if 1 <= n <= 7:
        return True
    return False


def win_condition_vertical(matrix, current_player, current_row, current_col):
    try:
        if matrix[current_row - 1][current_col] == current_player:
            if matrix[current_row - 2][current_col] == current_player:
                if matrix[current_row - 3][current_col] == current_player:
                    return True
        if matrix[current_row + 1][current_col] == current_player:
            if matrix[current_row + 2][current_col] == current_player:
                if matrix[current_row + 3][current_col] == current_player:
                    return True
    except IndexError:
        return False


def win_condition_horizontal(matrix, current_player, current_row, current_col):
    try:
        if matrix[current_row][current_col - 1] == current_player:
            if matrix[current_row][current_col - 2] == current_player:
                if matrix[current_row][current_col - 3] == current_player:
                    return True
        if matrix[current_row][current_col + 1] == current_player:
            if matrix[current_row][current_col + 2] == current_player:
                if matrix[current_row][current_col + 3] == current_player:
                    return True
    except IndexError:
        return False


def win_condition_diagonal(matrix, current_player, current_row, current_col):
    try:
        if matrix[current_row - 1][current_col - 1] == current_player:
            if matrix[current_row - 2][current_col - 2] == current_player:
                if matrix[current_row - 3][current_col - 3] == current_player:
                    return True
        if matrix[current_row - 1][current_col + 1] == current_player:
            if matrix[current_row - 2][current_col + 2] == current_player:
                if matrix[current_row - 3][current_col + 3] == current_player:
                    return True
        if matrix[current_row + 1][current_col - 1] == current_player:
            if matrix[current_row + 2][current_col - 2] == current_player:
                if matrix[current_row + 3][current_col - 3] == current_player:
                    return True
        if matrix[current_row + 1][current_col + 1] == current_player:
            if matrix[current_row + 2][current_col + 2] == current_player:
                if matrix[current_row + 3][current_col + 3] == current_player:
                    return True
    except IndexError:
        return False


def win_conditions(matrix, current_player, current_row, current_col):
    if win_condition_horizontal(matrix, current_player, current_row, current_col):
        return True
    elif win_condition_vertical(matrix, current_player, current_row, current_col):
        return True
    elif win_condition_diagonal(matrix, current_player, current_row, current_col):
        return True
    return False


we_have_a_winner = False
board = create_matrix()
while not we_have_a_winner:
    player_1 = 1
    player_2 = 2
    player_one_input = int(input('Player 1, please choose a column'))
    current_player = player_1
    if validation(player_one_input) and board[0][player_one_input] == 0:
        for row in range(5, -1, -1):
            if board[row][player_one_input - 1] == 0:
                board[row][player_one_input - 1] = current_player
                if win_conditions(board, current_player, row, (player_one_input - 1)):
                    print(f'The Winner is Player {current_player}')
                    we_have_a_winner = True
                    break
                pprint(board)
                break
        else:
            continue
    else:
        player_one_input = int(input())
        for row in range(5, -1, -1):
            if board[row][player_one_input - 1] == 0:
                board[row][player_one_input - 1] = current_player
                if win_conditions(board, current_player, row, (player_one_input - 1)):
                    print(f'The Winner is Player {current_player}')
                    we_have_a_winner = True
                    break
                pprint(board)
                break
    if we_have_a_winner:
        break

    player_two_input = int(input('Player 2, please choose a column'))
    current_player = player_2
    if validation(player_two_input) and board[0][player_two_input] == 0:
        for row in range(5, -1, -1):
            if board[row][player_two_input - 1] == 0:
                board[row][player_two_input - 1] = current_player
                if win_conditions(board, current_player, row, (player_two_input - 1)):
                    print(f'The Winner is Player {current_player}')
                    we_have_a_winner = True
                    break
                pprint(board)
                break
        else:
            continue
    else:
        player_two_input = int(input())
        for row in range(5, -1, -1):
            if board[row][player_two_input - 1] == 0:
                board[row][player_two_input - 1] = current_player
                if win_conditions(board, current_player, row, (player_two_input - 1)):
                    print(f'The Winner is Player {current_player}')
                    we_have_a_winner = True
                    break
                pprint(board)
                break
    if we_have_a_winner:
        break
pprint(board)