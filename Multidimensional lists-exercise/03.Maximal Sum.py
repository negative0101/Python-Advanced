rows, columns = [int(el) for el in input().split()]
matrix = []
for i in range(rows):
    matrix.append([int(i) for i in input().split()])
max_sum = 0
tree_by_tree_max_matrix = []
max_start_j, max_start_k = 0, 0

for j in range(rows - 2):
    for k in range(columns - 2):
        current_sum = sum([matrix[j][k], matrix[j][k + 1], matrix[j][k + 2],
                           matrix[j + 1][k], matrix[j + 1][k + 1], matrix[j + 1][k + 2],
                           matrix[j + 2][k], matrix[j + 2][k + 1], matrix[j + 2][k + 2]])
        if max_sum < current_sum:
            max_sum = current_sum
            max_start_j, max_start_k = j, k
print(f'Sum = {max_sum}')
for x in range(3):
    for y in range(3):
        print(matrix[max_start_j + x][max_start_k + y], end=' ')
    print()
