rows, columns = (input().split(', '))
matrix = []
for i in range(int(rows)):
    lines_of_elements = input().split()
    matrix.append(lines_of_elements)

for k in range(int(columns)):
    total_sum =0
    for j in range(int(rows)):
        total_sum += int(matrix[j][k])
    print(total_sum)