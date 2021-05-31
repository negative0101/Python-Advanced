row, column = [int(i) for i in input().split()]

matrix = []
number_of_matching_el = 0

for j in range(row):
    elements = input().split()
    matrix.append(elements)
for rows in range(row - 1):
    for columns in range(column - 1):
        if matrix[rows][columns] == matrix[rows][columns + 1] == matrix[rows + 1][columns] == matrix[rows + 1][columns + 1]:
            number_of_matching_el += 1

print(number_of_matching_el)
