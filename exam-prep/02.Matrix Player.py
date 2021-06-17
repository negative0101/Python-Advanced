def matrix_generator(n):
    matrix = []
    for i in range(n):
        current_word = []
        current_input = input()
        for j in current_input:
            current_word.append(j)
        matrix.append(current_word)
    return matrix


def index_checker_left(matrix, row, col):
    if 0 <= row < len(matrix) and 0 <= col - 1 < len(matrix):
        return True
    return False


def index_checker_right(matrix, row, col):
    if 0 <= row < len(matrix) and 0 <= col + 1 < len(matrix):
        return True
    return False


def index_checker_up(matrix, row, col):
    if 0 <= row - 1 < len(matrix) and 0 <= col < len(matrix):
        return True
    return False


def index_checker_down(matrix, row, col):
    if 0 <= row + 1 < len(matrix) and 0 <= col < len(matrix):
        return True
    return False


def locate_player(size_of_matrix, matrix):
    row_col = []
    for i in range(size_of_matrix):
        for j in range(size_of_matrix):
            if matrix[i][j] == 'P':
                row_col.append(i)
                row_col.append(j)
                return row_col


def player_moves_left(matrix, row, col):
    matrix[row][col - 1] = 'P'
    matrix[row][col] = '-'
    return matrix


def player_moves_right(matrix, row, col):
    matrix[row][col + 1] = 'P'
    matrix[row][col] = '-'
    return matrix


def player_moves_up(matrix, row, col):
    matrix[row - 1][col] = 'P'
    matrix[row][col] = '-'
    return matrix


def player_moves_down(matrix, row, col):
    matrix[row + 1][col] = 'P'
    matrix[row][col] = '-'
    return matrix


text = input()
n_square_matrix = int(input())
matrix = matrix_generator(n_square_matrix)

num_of_command = int(input())

for _ in range(num_of_command):
    row_col = locate_player(n_square_matrix, matrix)
    row, col = (map(int, row_col))
    command = input()
    if command == 'left':
        if index_checker_left(matrix, row, col):
            if matrix[row][col - 1] != '-':  # we found a letter to consume
                text += matrix[row][col - 1]
            player_moves_left(matrix, row, col)
        else:  # out of index
            if text:
                new_text = text[:len(text) - 1]
                text = new_text
            pass
    elif command == 'right':
        if index_checker_right(matrix, row, col):
            if matrix[row][col + 1] != '-':
                text += matrix[row][col + 1]
            player_moves_right(matrix, row, col)
        else:  # out of index
            if text:
                new_text = text[:len(text) - 1]
                text = new_text
            pass
    elif command == 'up':
        if index_checker_up(matrix, row, col):
            if matrix[row - 1][col] != '-':
                text += matrix[row - 1][col]
            player_moves_up(matrix, row, col)
        else:  # out of index
            if text:
                new_text = text[:len(text) - 1]
                text = new_text
            pass
    elif command == 'down':
        if index_checker_down(matrix, row, col):
            if matrix[row + 1][col] != '-':
                text += matrix[row + 1][col]
            player_moves_down(matrix, row, col)
        else:  # out of index
            if text:
                new_text = text[:len(text) - 1]
                text = new_text
            pass

print(text)
for x in range(len(matrix)):
    print(f'{"".join(matrix[x])}')
