def position_of_snake(mat):      # Check each time position of snake
    positions = []
    s_is_found = False
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] == 'S':
                positions.append(i)  # row
                positions.append(j)  # col
                s_is_found = True
                break
        if s_is_found:
            break

    return positions


def burrow(m):   # Burrow action to find and replace
    for i in range(len(m)):
        for j in range(len(m)):
            if m[i][j] == 'B':
                m[i][j] = 'S'
                return m

n = int(input())   # number of rows and columns for the matrix

is_out_of_matrix = False
food_quantity = 0
matrix = []
for i in range(n):  # filling up the matrix
    row = [i for i in input()]
    matrix.append(row)

command = input() # receive commands
while True:
    if food_quantity == 10:
        break

    snake_row, snake_col = position_of_snake(matrix)  # row and column for current position of snake

    if command == 'up':
        if 0 <= (snake_row - 1) < len(matrix):
            if matrix[snake_row - 1][snake_col] == '*':
                matrix[snake_row - 1][snake_col] = 'S'
                matrix[snake_row][snake_col] = '.'
                food_quantity += 1
            elif matrix[snake_row - 1][snake_col] == '-':
                matrix[snake_row - 1][snake_col] = 'S'
                matrix[snake_row][snake_col] = '.'
            elif matrix[snake_row - 1][snake_col] == 'B':  # Burrow action
                matrix[snake_row - 1][snake_col] = '.'
                matrix[snake_row][snake_col] = '.'
                matrix = burrow(matrix) # Burrow function
        else:
            is_out_of_matrix = True
            matrix[snake_row][snake_col] = '.'
            break

    elif command == 'down':
        if 0 <= snake_row + 1 < len(matrix):
            if matrix[snake_row + 1][snake_col] == '*':
                matrix[snake_row + 1][snake_col] = 'S'
                matrix[snake_row][snake_col] = '.'
                food_quantity += 1
            elif matrix[snake_row + 1][snake_col] == '-':
                matrix[snake_row + 1][snake_col] = 'S'
                matrix[snake_row][snake_col] = '.'
            elif matrix[snake_row + 1][snake_col] == 'B':  # Burrow action
                matrix[snake_row + 1][snake_col] = '.'
                matrix[snake_row][snake_col] = '.'
                matrix = burrow(matrix) #Burrow function
        else:
            is_out_of_matrix = True
            matrix[snake_row][snake_col] = '.'
            break

    elif command == 'left':
        if 0 <= snake_col - 1 < len(matrix):
            if matrix[snake_row][snake_col - 1] == '*':
                matrix[snake_row][snake_col - 1] = 'S'
                matrix[snake_row][snake_col] = '.'
                food_quantity += 1
            elif matrix[snake_row][snake_col - 1] == '-':
                matrix[snake_row][snake_col - 1] = 'S'
                matrix[snake_row][snake_col] = '.'
            elif matrix[snake_row][snake_col - 1] == 'B':  # Burrow action
                matrix[snake_row][snake_col - 1] = '.'
                matrix[snake_row][snake_col] = '.'
                matrix = burrow(matrix)
        else:
            is_out_of_matrix = True
            matrix[snake_row][snake_col] = '.'
            break

    elif command == 'right':
        if 0 <= snake_col + 1 < len(matrix):
            if matrix[snake_row][snake_col + 1] == '*':
                matrix[snake_row][snake_col + 1] = 'S'
                matrix[snake_row][snake_col] = '.'
                food_quantity += 1
            elif matrix[snake_row][snake_col + 1] == '-':
                matrix[snake_row][snake_col + 1] = 'S'
                matrix[snake_row][snake_col] = '.'
            elif matrix[snake_row][snake_col + 1] == 'B':  # Burrow action
                matrix[snake_row][snake_col + 1] = '.'
                matrix[snake_row][snake_col] = '.'
                matrix = burrow(matrix)
        else:
            is_out_of_matrix = True
            matrix[snake_row][snake_col] = '.'
            break

    if food_quantity >= 10:
        print(f'You won! You fed the snake.')
        print(f'Food eaten: {food_quantity}')
        break

    command = input()

if is_out_of_matrix:
    print(f'Game over!')
    print(f'Food eaten: {food_quantity}')

for row in range(len(matrix)):
    print(''.join(matrix[row]))