def find_miner(matrix):
    row_col = []
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == 's':
                row_col.append(row)
                row_col.append(col)
                return row_col


def index_checker(matrix, row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        return True
    return False


def total_coal_in_matrix(matrix):
    total_coal = 0
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == 'c':
                total_coal += 1
    return total_coal


num = int(input())
commands = [_ for _ in input().split()]

matrix = [input().split() for _ in range(num)]

player_row, player_col = find_miner(matrix)
total_coal = total_coal_in_matrix(matrix)
game_over = False

current_coal = 0

for command in commands:
    player_row, player_col = find_miner(matrix)
    if command == 'up':
        if index_checker(matrix, player_row - 1, player_col):
            if matrix[player_row - 1][player_col] == 'c':
                current_coal += 1
                matrix[player_row][player_col], matrix[player_row - 1][player_col] = '*', 's'
                if total_coal == current_coal:
                    print(f"You collected all coals! ({player_row - 1}, {player_col})")
                    break
            elif matrix[player_row - 1][player_col] == 'e':
                print(f'Game over! ({player_row - 1}, {player_col})')
                game_over = True

                break
            else:
                matrix[player_row][player_col], matrix[player_row - 1][player_col] = '*', 's'
        else:
            continue
    elif command == 'down':
        if index_checker(matrix, player_row + 1, player_col):
            if matrix[player_row + 1][player_col] == 'c':
                current_coal += 1
                matrix[player_row][player_col], matrix[player_row + 1][player_col] = '*', 's'
                if total_coal == current_coal:
                    print(f"You collected all coals! ({player_row + 1}, {player_col})")
                    break
            elif matrix[player_row + 1][player_col] == 'e':
                print(f'Game over! ({player_row + 1}, {player_col})')
                game_over = True
                break
            else:
                matrix[player_row][player_col], matrix[player_row + 1][player_col] = '*', 's'
        else:
            continue
    elif command == 'left':
        if index_checker(matrix, player_row, player_col - 1):
            if matrix[player_row][player_col - 1] == 'c':
                current_coal += 1
                matrix[player_row][player_col], matrix[player_row][player_col - 1] = '*', 's'
                if total_coal == current_coal:
                    print(f"You collected all coals! ({player_row}, {player_col - 1})")
                    break
            elif matrix[player_row][player_col - 1] == 'e':
                print(f'Game over! ({player_row}, {player_col - 1})')
                game_over = True

                break
            else:
                matrix[player_row][player_col], matrix[player_row][player_col - 1] = '*', 's'
        else:
            continue
    elif command == 'right':
        if index_checker(matrix, player_row, player_col + 1):
            if matrix[player_row][player_col + 1] == 'c':
                current_coal += 1
                matrix[player_row][player_col], matrix[player_row][player_col + 1] = '*', 's'
                if total_coal == current_coal:
                    print(f"You collected all coals! ({player_row}, {player_col + 1})")
                    break
            elif matrix[player_row][player_col + 1] == 'e':
                print(f'Game over! ({player_row}, {player_col + 1})')
                game_over = True
                break
            else:
                matrix[player_row][player_col], matrix[player_row][player_col + 1] = '*', 's'
        else:
            continue
player_row, player_col = find_miner(matrix)

if current_coal != total_coal and not game_over:
    print(f"{total_coal - current_coal} coals left. ({player_row}, {player_col})")
