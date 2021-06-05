
def index_checker(r, c):
    if 0 <= r < len(matrix) and 0 <= c < len(matrix):
        return True
    return False


n = int(input())
matrix =[[int(j) for j in input().split()] for i in range(int(n))]

command = input()
while not command == 'END':
    type_command, row, col, value = command.split()
    row, col, value = int(row), int(col), int(value)
    if type_command == 'Add':
        if index_checker(row,col):
            matrix[row][col] += value
        else:
            print(f'Invalid coordinates')
    elif type_command == 'Subtract':
        if index_checker(row,col):
            matrix[row][col] -= value
        else:
            print('Invalid coordinates')

    command = input()
print('\n'.join(' '.join([str(el) for el in x]) for x in matrix))