rows, columns = input().split(', ')
matrix = []
max_pair = 0
first_line = []
second_line = []
for i in range(int(rows)):
    elements_per_row = input().split(', ')
    elements_per_row = list(map(int, elements_per_row))
    matrix.append(elements_per_row)
for j in range(int(rows)-1 ):
    for k in range(int(columns)-1 ):
        if ((matrix[j][k] + matrix[j][k + 1]) + (matrix[j + 1][k] + matrix[j + 1][k + 1])) > max_pair:
            first_line = []
            second_line = []
            first_line.append(matrix[j][k])
            first_line.append(matrix[j][k+1])
            second_line.append(matrix[j+1][k])
            second_line.append(matrix[j+1][k+1])
            max_pair = sum(first_line + second_line)
print(*first_line)
print(*second_line)
print(max_pair)