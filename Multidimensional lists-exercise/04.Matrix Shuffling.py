def printing(m):
    for j in range(rows):
        for k in range(columns):
            print(m[j][k], end=' ')
        print()


rows, columns = [int(_) for _ in input().split()]

matrix = []
for r in range(rows):
    matrix.append(input().split())

command = input()
while not command == 'END':
    command = command.split()
    if command[0] == 'swap' and len(command) == 5:
        row1 = int(command[1])
        col1 = int(command[2])
        new_row1 = int(command[3])
        new_col2 = int(command[4])
        try:
            matrix[row1][col1], matrix[new_row1][new_col2] = matrix[new_row1][new_col2], matrix[row1][col1]
            printing(matrix)
        except IndexError:
            print(f'Invalid input!')
    else:
        print(f'Invalid input!')

    command = input()
