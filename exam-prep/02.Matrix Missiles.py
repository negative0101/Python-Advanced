import math


def create_matrix():
    matrix = []

    for row in range(7):
        matrix.append(input().split())
    return matrix


def check_current_player(turn):
    if turn % 2 == 0:
        return player_2_score
    return player_1_score


player_1_name, player_2_name = input().split(', ')
matrix = create_matrix()
player_1_score = 501
player_2_score = 501
turn = 0
current_player = 0

winner_found = False
while player_1_score > 0 and player_2_score > 0:
    turn += 1
    row_col = input()

    row = int(row_col[1])
    col = int(row_col[4])
    current_player = check_current_player(turn)
    try:
        if matrix[row][col].isnumeric():
            current_player -= int(matrix[row][col])
            if turn % 2 == 0:
                player_2_score = current_player
            else:
                player_1_score = current_player
        elif matrix[row][col] == 'D':

            sum_of_d = (int(matrix[row][0]) + int(matrix[0][col]) + int(matrix[row][-1]) + int(matrix[-1][col])) * 2
            current_player -= sum_of_d
            if turn % 2 == 0:
                player_2_score = current_player
            else:
                player_1_score = current_player
        elif matrix[row][col] == 'T':
            sum_of_t = (int(matrix[row][0]) + int(matrix[0][col]) + int(matrix[row][-1]) + int(matrix[-1][col])) * 3
            current_player -= sum_of_t
            if turn % 2 == 0:
                player_2_score = current_player
            else:
                player_1_score = current_player
        elif matrix[row][col] == 'B':
            break

    except IndexError:
        continue

if not turn % 2 == 0:
    print(f'{player_1_name} won the game with {math.ceil(turn / 2)} throws!')

else:
    print(f'{player_2_name} won the game with {math.ceil(turn / 2)} throws!')
