rows, columns = (input().split(', '))
matrix = []
total_sum = 0
for i in range(int(rows)):
    matrix.append([])
    lines_of_elements = input().split(', ')
    for j in range(int(columns)):
        matrix[i].append(int(lines_of_elements[j]))
        total_sum += int(lines_of_elements[j])
print(total_sum)
print(matrix)
