def create_blank_matrix(n):
    m = []
    for _ in range(n):
        m.append([])
        for _ in range(n):
            m[-1].append(0)
    return m


def same_row_left(row, col, matrix):
    if 0 <= col - 1 < len(matrix):
        if matrix[row][col - 1] == '*':
            matrix[row][col] += 1
        return matrix


def same_row_right(row, col, matrix):
    if 0 <= col + 1 < len(matrix):
        if matrix[row][col + 1] == '*':
            matrix[row][col] += 1
        return matrix


def above_same_row(row, col, matrix):
    if 0 <= row - 1 < len(matrix):  # one above
        if matrix[row - 1][col] == '*':
            matrix[row][col] += 1
        return matrix


def above_one_right(row, col, matrix):
    if 0 <= col + 1 < len(matrix) and 0 <= row - 1 < len(matrix):  # one above and right
        if matrix[row - 1][col + 1] == '*':
            matrix[row][col] += 1
        return matrix


def above_one_left(row, col, matrix):
    if 0 <= col - 1 < len(matrix) and 0 <= row - 1 < len(matrix):  # one above and left
        if matrix[row - 1][col - 1] == '*':
            matrix[row][col] += 1
        return matrix


def below_same_row(row, col, matrix):
    if 0 <= row + 1 < len(matrix):  # one below
        if matrix[row + 1][col] == '*':
            matrix[row][col] += 1
        return matrix


def below_one_left(row, col, matrix):
    if 0 <= col - 1 < len(matrix) and 0 <= row + 1 < len(matrix):
        if matrix[row + 1][col - 1] == '*':  # left
            matrix[row][col] += 1
        return matrix


def below_one_right(row, col, matrix):
    if 0 <= col + 1 < len(matrix) and 0 <= row + 1 < len(matrix):  # right
        if matrix[row + 1][col + 1] == '*':
            matrix[row][col] += 1
        return matrix


num = int(input())
bombs = int(input())

matrix = create_blank_matrix(num)

for i in range(bombs):
    bomb_row_and_column = input()
    bombs_row = int(bomb_row_and_column[1])
    bombs_column = int(bomb_row_and_column[4])
    if 0 <= bombs_row < len(matrix) and 0 <= bombs_column < len(matrix):
        matrix[bombs_row][bombs_column] = '*'  # -> bomb is planted

for row in range(num):
    for col in range(num):
        if matrix[row][col] != '*':
            same_row_left(row, col, matrix)
            same_row_right(row, col, matrix)
            above_same_row(row, col, matrix)
            above_one_right(row, col, matrix)
            above_one_left(row, col, matrix)
            below_same_row(row, col, matrix)
            below_one_left(row, col, matrix)
            below_one_right(row, col, matrix)

for x in range(num):
    for y in range(num):
        print(matrix[x][y], end=' ')
    print()
